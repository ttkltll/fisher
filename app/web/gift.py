from flask_login import login_required

from . import web
__author__ = '七月'


@web.route('/my/gifts')
def my_gifts():
    pass


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass


@login_required
@web.route('/gifts/')

def gift():
    if not_login:
        url = request.url
        return redirect(/login/?=url),要带上现在的url,以便可以返回回来，怎么实现？
    return 'Gift'

