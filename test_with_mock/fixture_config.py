import pytest
'''
import pytest

from main import app, app_db
@pytest.fixture
def api(mocker):
    mocker.patch("flask_sqlalchemy.SQLAlchemy.init_app", return_value=True)
    mocker.patch("flask_sqlalchemy.SQLAlchemy.create_all", return_value=True)
    api = app.test_client()
    yield api


import json
def test_get_contents(api):
    get_resp = api.get(
        f'{"v1/board-service/contents"}'
    )
    get_resp_json = json.loads(get_resp.data.decode('utf-8'))
    print(get_resp_json)
    assert get_resp_json['data']['content_dto']['id'] == 1
    assert get_resp_json['code'] == 200

'''
'''
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
'''