'''
terminal command >> pytest -s -vv
'''
import json
from .fixture_config import *

########## integration test : router ##########

def test_get_version_2_board_service_content(api):
    get_resp = api.get(
        f'{"v2/board-service/content/"}{1}'
    )
    get_resp_json = json.loads(get_resp.data.decode('utf-8'))
    assert get_resp_json['data']['content_dto']['id'] == 1
    assert get_resp_json['code'] == 200


def test_not_support_version_0(api):
    get_resp = api.get(
        f'{"v0/monitoring-service/content/"}{1}'
    )
    print(get_resp.data.decode('utf-8'))
    #get_resp_json = json.loads(get_resp.data.decode('utf-8'))
    #assert get_resp_json['code'] == 404