import pytest


@pytest.fixture()
def api():
    from main import app, app_db as db
    from main.model.content import Content
    with app.app_context():
        db.create_all()

    with app.app_context():
        from main.model.db_manage import transaction
        with transaction():
            content = Content('{"author":"manager","title":"title0"}')
            db.session.add(content)
        # teardown_app_context decorator activate
    api = app.test_client()
    yield api

    with app.app_context():
        db.drop_all()


