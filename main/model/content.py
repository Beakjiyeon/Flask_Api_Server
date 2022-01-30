from .. import app_db as db
from ..dto.content_dto import ContentDto


class Content(db.Model):
    __tablename__ = 'content'
    id = db.Column(db.BigInteger, primary_key=True)
    data_info = db.Column(db.String(255))
    reg_date = db.Column(db.DATETIME, server_default=db.func.current_timestamp())  # 'default' / None
    mod_date = db.Column(db.DATETIME)

    def __init__(self, *args, **kwargs):
        if 'id' in kwargs:
            self.id = kwargs['id']
        else:
            self.id = None
        self.data_info = args[0]
        self.reg_date = None
        self.mod_date = None
