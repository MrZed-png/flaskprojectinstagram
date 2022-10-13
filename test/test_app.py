import pytest
from run import app


def test_app_all_posts_status_code():
    """Проверяет статус код и тип файла"""
    response = app.test_client().get('/api/posts', follow_redirects=True)
    assert response.status_code == 200, "Статус код запроса не верный"
    assert response.mimetype == "application/json", "Получен не JSON"


def test_app_all_posts_type_count_content():
    """Проверяем в каком формате пришел фаил"""
    response = app.test_client('/api/posts', follow_redirects=True)
    assert type(response.json) == list, "Получен не список"


def test_api_single_post_status_code_and_type():
    """Проверка 1 поста"""
    response = app.test_client('/api/posts/1', follow_redirects=True)
    assert response.status_code == 200, "Статус код запроса не верный"
    assert response.mimetype == "application/json", "Получен не JSON"
    assert type(response.json) == dict, "Получен не словарь"