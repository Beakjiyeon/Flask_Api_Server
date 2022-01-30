class ContentDto():
    def __init__(self, entity):
        self.id = entity.id
        self.data_info = entity.data_info
        # self.reg_date = None
        self.mod_date = get_entity_date(entity.mod_date)


def get_entity_date(entity_date):
    if entity_date is not None:
        return entity_date.strftime('%Y-%m-%d %H:%M:%S')


