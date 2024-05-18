"""
@author: harumonia
@license: © Copyright 2024, Node Supply Chain Manager Corporation Limited.
@contact: zxjlm233@gmail.com
@software: Pycharm
@homepage: https://harumonia.moe/
@file: resp_models.py
@time: 2024/5/18 22:46
@desc:
"""
import typing

from pydantic import BaseModel, Field


class CommonErrorResp(BaseModel):
    msg: str = Field(description="message")


class FontResp(BaseModel):
    name: str = Field(description="")
    img: str = Field(description="图像 base64")
    ocr_result: str = Field(description="识别结果")


class LocalCrackerResp(BaseModel):
    spend_time: int = Field(description="")
    raw_out: typing.List[FontResp] = Field(description="")
