from flask import Blueprint, redirect, url_for, jsonify

api_v0 = Blueprint('api_v0', __name__, url_prefix='/v0')

from ...dto.response import *


@api_v0.route('', defaults={'path': ''})
@api_v0.route('/<path:path>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def v0(path):
    raise ApiException(ResponseCode.ILLEGAL_VERSION.code, ResponseCode.ILLEGAL_VERSION.message)
