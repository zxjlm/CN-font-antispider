"""
@author: harumonia
@license: © Copyright 2024, Node Supply Chain Manager Corporation Limited.
@contact: zxjlm233@gmail.com
@software: Pycharm
@homepage: https://harumonia.moe/
@file: generate_openapi.py
@time: 2024/5/18 22:56
@desc:
"""

from fastapi.openapi.utils import get_openapi
from app.main import app
import json

with open('openapi.json', 'w') as f:
    json.dump(get_openapi(
        title="Poirot",
        version="0.1",
        # openapi_version=app.openapi_version,
        # description=app.description,
        routes=app.routes,
        # openapi_prefix=app.openapi_prefix,
    ), f)
