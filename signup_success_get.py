from bottle import get, view

from check_if_logged_in import check_if_logged_in

@get("/signup-success")
@view("signup_success.html")
def signup_success_view():
    return dict(is_logged_in=check_if_logged_in())
