
from flask import Flask, make_response, Request

from helper import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """

    :param q: 普通关键字，isbn
    :param page:
    :return:
    """
    # alt+enter:导入模块
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return result

def helloo():
    return 'Hello QiYue'


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=81)


