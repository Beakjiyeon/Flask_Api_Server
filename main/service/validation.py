from ..dto.response import *

def validate_board(params):
    if params == None:
        raise ParameterException(ResponseCode.NULL_PARAMETER.code, ResponseCode.NULL_PARAMETER.message)
    missing_fields = {'data_info'}
    missing_fields = missing_fields - params.keys()
    if len(missing_fields) > 0:
        raise ParameterException(ResponseCode.NULL_PARAMETER.code,
                                 f"필수 필드 {missing_fields}가 누락되었습니다.")
    if not type(params['data_info']) == str: # isinstance()
        raise ParameterException(ResponseCode.ILLEGAL_PARAMETER.code,
                                 f"{ResponseCode.ILLEGAL_PARAMETER.message} data_info 필드가 str 타입이 아닙니다.")
    if len(params['data_info']) == 0:
        raise ParameterException(ResponseCode.ILLEGAL_PARAMETER.code,
                                 f"{ResponseCode.ILLEGAL_PARAMETER.message} data_info 필드가 빈 값입니다.")


# 404 url 요청 시, 로그에 사용될 서비스명 항목 유효성 검사
def validate_request_service(url):
    temp = url.split('/')
    if len(temp) <= 4: # http, '', ip, version, service
        return False
    version = url.split('/')[3]
    service = url.split('/')[4]
    if version == None or service == None:
        return False
    api_versions = ['v0', 'v1', 'v2']
    api_services = ['board-service', 'monitoring-service', 'query-service']
    if version not in api_versions or service not in api_services:
        return False
    return True