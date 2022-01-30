from ..model.content import Content
from ..service.validation import *
from ..dto.response import *
from ..dto.content_dto import *
from .. import app_db as db
from ..model.db_manage import transaction


class BoardService:
    def create_board(self, params):
        validate_board(params)
        with transaction():
            content = Content(params['data_info'])
            db.session.add(content) # 2
        result = Content.query.get_or_404(content.id)
        return ContentDto(result)


    def get_boards(self):
        contents = Content.query.all()
        return [ContentDto(content).__dict__ for content in contents]


    def get_board_by_id(self, id):
        content = Content.query.get_or_404(id)
        return ContentDto(content)


    def update_board_by_id(self, id, params):
        validate_board(params)
        content = Content.query.get_or_404(id) # 404 에러, tranaction 500 에러 구분을 위함
        with transaction():
            content.data_info = params['data_info']
        result = Content.query.get_or_404(id)
        return ContentDto(content)


    def delete_board_by_id(self, id):
        content = Content.query.get_or_404(id)
        with transaction():
            db.session.delete(content)
        return id