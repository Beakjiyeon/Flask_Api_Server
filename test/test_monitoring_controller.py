'''
terminal command >> pytest -s -vv
'''
import json
from .fixture_config import *

########## integration test : router ##########
def test_get_monitoring_service_content(api):
    get_resp = api.get(
        f'{"v1/monitoring-service/content/"}{1}'
    )
    get_resp_json = json.loads(get_resp.data.decode('utf-8'))
    assert get_resp_json['data']['content_dto']['id'] == 1
    assert get_resp_json['code'] == 200
