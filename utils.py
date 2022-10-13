import json


def load_posts() -> list[dict]:
    """Выгружает данные постов"""
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def load_comments() -> list[dict]:
    """Выгружает данные коментариев"""
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_all():
    """возвращает посты"""
    result = load_posts()
    return result


def get_posts_by_user(user_name):
    """возвращает посты определенного пользователя."""
    result = []
    for post in load_posts():
        if user_name.lower() in post['poster_name'].lower():
            result.append(post)
    return result


def get_comments_by_post_id(post_id):
    """возвращает комментарии определенного поста."""
    result = []
    for post in load_comments():
        if post_id == post['post_id']:
            result.append(post)
    return result


def search_for_posts(query: str) -> list[dict]:
    """возвращает список постов по ключевому слову"""
    result = []
    for post in load_posts():
        if query.lower() in post['content'].lower():
            result.append(post)
    return result


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору."""
    for post in load_posts():
        if pk == post['pk']:
            return post
