from flask import Blueprint
board_api = Blueprint('board_api_v0', __name__, url_prefix='/v0/board-service')


from ...service.board_service import BoardService
boardService = BoardService()


from flask import request, jsonify
from ...dto.response import *
from flask import g


@board_api.route('/content', methods=['POST'])
def create_content():
    params = request.get_json()
    contentDto = boardService.create_board(params)
    g.test['content_dto'] = contentDto.__dict__
    return ApiResponse(ResponseCode.OK.code, ResponseCode.OK.message, g.test)


@board_api.route('/contents', methods=['GET'])
def get_contents():
    contentDtos = boardService.get_boards()
    g.test['content_dtos'] = contentDtos
    return ApiResponse(ResponseCode.OK.code, ResponseCode.OK.message, g.test)


@board_api.route('/content/<int:id>', methods=['GET'])
def get_content(id):
    contentDto = boardService.get_board_by_id(id)
    g.test['content_dto'] = contentDto.__dict__
    return ApiResponse(ResponseCode.OK.code, ResponseCode.OK.message, g.test)


@board_api.route('/content/<int:id>', methods=['PUT'])
def update_content(id):
    params = request.get_json()
    contentDto = boardService.update_board_by_id(id, params)
    g.test['content_dto'] = contentDto.__dict__
    return ApiResponse(ResponseCode.OK.code, ResponseCode.OK.message, g.test)


@board_api.route('/content/<int:id>', methods=['DELETE'])
def delete_content(id):
    delete_id = boardService.delete_board_by_id(id)
    g.test['id'] = delete_id
    return ApiResponse(ResponseCode.OK.code, ResponseCode.OK.message, g.test)

