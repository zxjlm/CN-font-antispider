import copy
import logging
import traceback

from PIL import Image

from config import model_path, crnn_model_path, angle_detect, angle_net_path, \
    angle_detect_num, is_rgb
from local_ocr.angnet import AngleNetHandle
from local_ocr.crnn import CRNNHandle
from local_ocr.dbnet.dbnet_infer import DBNET
from local_ocr.utils import sorted_boxes, get_rotate_crop_image
import numpy as np


class OcrHandle(object):
    def __init__(self):
        self.text_handle = DBNET(model_path)
        self.crnn_handle = CRNNHandle(crnn_model_path)
        if angle_detect:
            self.angle_handle = AngleNetHandle(angle_net_path)

    def crnnRecWithBox(self, im, boxes_list, score_list):
        """
        crnn模型，ocr识别
        @@model,
        @@converter,
        @@im:Array
        @@text_recs:text box
        @@ifIm:是否输出box对应的img

        """
        results = []
        boxes_list = sorted_boxes(np.array(boxes_list))

        line_imgs = []
        for index, (box, score) in enumerate(zip(boxes_list[:angle_detect_num],
                                                 score_list[
                                                 :angle_detect_num])):
            tmp_box = copy.deepcopy(box)
            partImg_array = get_rotate_crop_image(im,
                                                  tmp_box.astype(np.float32))
            partImg = Image.fromarray(partImg_array).convert("RGB")
            line_imgs.append(partImg)

        angle_res = False
        if angle_detect:
            angle_res = self.angle_handle.predict_rbgs(line_imgs)

        count = 1
        for index, (box, score) in enumerate(zip(boxes_list, score_list)):

            tmp_box = copy.deepcopy(box)
            partImg_array = get_rotate_crop_image(im,
                                                  tmp_box.astype(np.float32))

            partImg = Image.fromarray(partImg_array).convert("RGB")

            if angle_detect and angle_res:
                partImg = partImg.rotate(180)

            if not is_rgb:
                partImg = partImg.convert('L')

            try:
                if is_rgb:
                    simPred = self.crnn_handle.predict_rbg(partImg)
                else:
                    simPred = self.crnn_handle.predict(partImg)
            except Exception as _e:
                print(traceback.format_exc())
                logging.info(_e)
                continue

            if simPred.strip() != '':
                results.append({"simPred": simPred, "score": float(score)})
                count += 1

        return results

    def text_predict(self, img):
        boxes_list, score_list = self.text_handle.process(
            np.asarray(img).astype(np.uint8))
        result = self.crnnRecWithBox(np.array(img), boxes_list, score_list)

        return result


if __name__ == "__main__":
    pass
