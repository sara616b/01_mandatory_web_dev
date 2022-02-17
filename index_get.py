from bottle import get, view

from global_values import *
from check_if_logged_in import check_if_logged_in

@get("/")
@view("index.html")
def index_view():
    return dict(is_logged_in=check_if_logged_in())
