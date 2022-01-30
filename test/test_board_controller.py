'''
terminal command >> pytest -s -vv
'''
import json
from .fixture_config import *
# from .fixture_config import *

######### integration test : read ##########

def test_get_content(api):
    get_resp = api.get(
        f'{"v1/board-service/content/"}{1}'
    )
    get_resp_json = json.loads(get_resp.data.decode('utf-8'))
    assert get_resp_json['data']['content_dto']['id'] == 1
    assert get_resp_json['code'] == 200


def test_get_content_not_exist(api):
    get_resp = api.get(
        f'{"v1/board-service/content/"}{2}'
    )
    get_resp_json = json.loads(get_resp.data.decode('utf-8'))
    assert get_resp_json['code'] == 404


def test_get_content_by_not_allowed_method(api):
    get_resp = api.post(
        f'{"v1/board-service/content/"}{1}',
        content_type='application/json'
    )
    get_resp_json = json.loads(get_resp.data.decode('utf-8'))
    assert get_resp_json['code'] == 405


def test_get_contents(api):
    resp = api.get(
        'v1/board-service/contents',
    )
    resp_json = json.loads(resp.data.decode('utf-8'))
    assert len(resp_json['data']) == 1



########## integration test : create ##########

def test_create_content(api):
    new_content = {
        'data_info': '{"author":"user2","title":"title2"}'
    }
    resp = api.post(
        'v1/board-service/content',
        data=json.dumps(new_content),
        content_type='application/json'
    )
    resp_json = json.loads(resp.data.decode('utf-8'))
    print(resp_json)
    assert resp_json['code'] == 200
    assert resp_json['data']['content_dto']['id'] == 2



def test_create_content_with_null_parameter(api):
    resp = api.post(
        'v1/board-service/content'
    )
    resp_json = json.loads(resp.data.decode('utf-8'))
    assert resp_json['code'] == 400


def test_create_content_with_illegal_parameter(api):
    new_content = {
        'data_info': 1
    }
    resp = api.post(
        'v1/board-service/content',
        data=json.dumps(new_content),
        content_type='application/json'
    )
    resp_json = json.loads(resp.data.decode('utf-8'))
    assert resp_json['code'] == 400



########## integration test : update ##########

def test_update_content(api):
    update_content = {
        'data_info': '{"author":"user1","title":"title1_updated"}'
    }
    update_resp = api.put(
        f'{"v1/board-service/content/"}{1}',
        data=json.dumps(update_content),
        content_type='application/json',
    )
    update_resp_json = json.loads(update_resp.data.decode('utf-8'))
    assert update_resp_json['data']['content_dto']['data_info'] == '{"author":"user1","title":"title1_updated"}'


def test_update_content_not_exist(api):
    update_content = {
        'data_info': '{"author":"user1","title":"title1_updated"}'
    }
    update_resp = api.put(
        f'{"v1/board-service/content/"}{12345}',
        data=json.dumps(update_content),
        content_type='application/json',
    )
    update_resp_json = json.loads(update_resp.data.decode('utf-8'))
    print('>> ', update_resp_json)
    assert update_resp_json['code'] == 404


def test_update_content_with_null_parameter(api):
    update_content = {}
    update_resp = api.put(
        f'{"v1/board-service/content/"}{1}',
        data=json.dumps(update_content),
        content_type='application/json',
    )
    update_resp_json = json.loads(update_resp.data.decode('utf-8'))
    assert update_resp_json['code'] == 400


def test_update_content_with_illegal_parameter(api):
    update_content = {
        'data_info': 1
    }
    update_resp = api.put(
        f'{"v1/board-service/content/"}{1}',
        data=json.dumps(update_content),
        content_type='application/json',
    )
    update_resp_json = json.loads(update_resp.data.decode('utf-8'))
    assert update_resp_json['code'] == 400



########## integration test : delete ##########

def test_delete_content(api):
    delete_resp = api.delete(
        f'{"v1/board-service/content/"}{1}',
        content_type='application/json'
    )
    delete_resp_json = json.loads(delete_resp.data.decode('utf-8'))
    assert delete_resp_json['data']['id'] == 1


def test_delete_content_not_exist(api):
    delete_resp = api.delete(
        f'{"v1/board-service/content/"}{0}',
        content_type='application/json'
    )
    delete_resp_json = json.loads(delete_resp.data.decode('utf-8'))
    assert delete_resp_json['code'] == 404

