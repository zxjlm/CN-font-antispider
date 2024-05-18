import os
import re
import time
import typing

from fastapi import APIRouter, UploadFile
from starlette.requests import Request

from app import config
from app.schemas.resp_models import FontResp, CommonErrorResp, LocalCrackerResp
from app.utils.ocrs import check_file, ocr_processor, ocr_func

add_response = {400: {"model": CommonErrorResp}}
font_api_router = APIRouter(responses=add_response)


@font_api_router.post('/font_file_cracker/', response_model=typing.List[FontResp])
async def font_file_cracker(file: UploadFile):
    filename = re.sub('[（(）) ]', '', file.filename)

    base_path = './font_collection'
    if not os.path.exists(base_path):
        os.mkdir(base_path)

    font_path = os.path.join(base_path, filename)
    with open(font_path, "wb") as f:
        f.write(await file.read())

    if config.is_online and not check_file(font_path):
        return {'msg': 'Please use example file(*^_^*)'}

    res = ocr_processor(font_path)

    return res


@font_api_router.post('/img_cracker_via_local_ocr/', response_model=LocalCrackerResp)
async def local_cracker(img_b64: str, request: Request):
    """
    接受单个图片，进行本地的ocr，返回图片破解结果
    :return:
    """
    if config.is_online:
        return {'msg': 'online mode can`t use image cracker'}
    # img_b64 = request.form['img'].replace('data:image/png;base64,', '')

    start_time = time.time()
    res = ocr_func(img_b64, 'single_image', request.client.host)
    return {'raw_out': res,
            'spend_time':
                round(time.time() - start_time, 2)}
