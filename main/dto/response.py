from flask import Response
import json

from enum import Enum
class ResponseCode(Enum):
    OK = (200, '실행을 성공적으로 완료하였습니다.')
    NULL_PARAMETER = (400, '필수 인자가 누락되었습니다.')
    ILLEGAL_PARAMETER = (400, '유효하지 않은 인자입니다.')
    ERROR = (500, '내부서버에서 오류가 발생하였습니다.')
    ILLEGAL_VERSION = (404, '지원하지 않는 API 버전입니다.')

    def __init__(self, code, message):
        self.code = code
        self.message = message


class ApiResponse(Response):
    def __init__(self, *args): # args = [status_code, message, data]
        result = {
            "code" : args[0],
            "message" : args[1]
        }
        if len(args) == 3:
            result["data"] = args[2]
        super(ApiResponse, self).__init__(json.dumps(result, ensure_ascii=False))
    default_mimetype = 'application/json'


class ParameterException(Exception):
    def __init__(self, code, error_message):
        self.code = code
        self.error_message = error_message


class ApiException(Exception):
    def __init__(self, code, error_message):
        self.code = code
        self.error_message = error_message

