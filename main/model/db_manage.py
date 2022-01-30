from .. import app_db as db
from ..dto.response import *

from contextlib import contextmanager


@contextmanager
def transaction():
    try:
        # 1
        yield  # 2 (호출 지점 처리)
        # ['SQLALCHEMY_COMMIT_ON_TEARDOWN'] is dangerous.
        db.session.commit()  # 3
    except Exception as e:
        print('롤백을 수행합니다.')
        db.session.rollback()
        raise ApiException(ResponseCode.ERROR.code, ResponseCode.ERROR.message)


'''
# reference
https://planbs.tistory.com/entry/Engine%EA%B3%BC-Session-Scoped-Session
https://saswatac.medium.com/transactions-using-flask-sqlalchemy-f5b26d23e2f2
'''
