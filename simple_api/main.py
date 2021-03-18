import re

import uvicorn
from fastapi import FastAPI, File, UploadFile

from utils import single_font_to_pic

app = FastAPI()


@app.post('/api/special_for_printed_digits/')
async def special_for_printed_digits(file: UploadFile = File(...)):
    """
    针对数字进行特化
    Returns:

    """
    filename = re.sub('[（(）) ]', '', file.filename)

    res = single_font_to_pic(file.filename, file.file.read())
    return {'code': 200, 'font_dict': {foo['name']: int(foo['ocr_result']) for foo in res}}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5001)
