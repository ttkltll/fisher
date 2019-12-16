from flask import jsonify

from fisher import app
from helper import is_isbn_or_key
from yushu_book import YuShuBook


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
    return jsonify(result)
    #return json.dumps(result), 200, {'content-type': 'application/json'}



