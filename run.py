import logging
from json import JSONDecodeError

from flask import Flask, request, render_template, send_from_directory, jsonify
# from functions import ...
import utils
from utils import get_posts_all, search_for_posts, get_post_by_pk, get_comments_by_post_id, get_posts_by_user

app = Flask(__name__)


@app.route('/')
def main_page():
    """реализация ленты"""
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/search/')
def search_page():
    """реализация поиска"""
    search_query = request.args.get('s', '')
    posts = search_for_posts(search_query)
    posts_amount = len(posts)
    return render_template('search.html',
                           queue=search_query,
                           posts=posts,
                           posts_amount=posts_amount)


@app.route('/post/<int:post_id>')
def post_page(post_id):
    """реализация просмотра поста"""
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    comments_amount = len(comments)
    return render_template('post.html', post=post,
                           comments=comments,
                           comments_amount=comments_amount)


@app.route('/users/<username>')
def users_page(username):
    """Реализация вывода по пользователю"""
    posts = get_posts_by_user(username)
    user_name = username
    return render_template('user-feed.html', posts=posts, user_name=user_name)


@app.errorhandler(404)
def error_404(error_code):
    print(f'Возникла ошибка {error_code}')
    return 'Упс, страница, которую вы искали не существует, код ошибки - 404'


@app.errorhandler(500)
def error_500(error_code):
    print(f'Возникла ошибка {error_code}')
    return 'Возникла ошибка со стороны сервера, код ошибки - 500'


@app.route('/api/posts')
def read_books():
    post = utils.load_posts()
    logging.info('request /api/posts/')
    return jsonify(post)


@app.route('/api/posts/<int:post_id>')
def read_book(post_id):
    post = utils.get_post_by_pk(post_id)
    logging.info(f'request /api/posts/{post_id}')
    return jsonify(post)


logging.basicConfig(filename='logs/api.log', level=logging.INFO)

app.run()
