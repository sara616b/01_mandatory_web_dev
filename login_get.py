from bottle import get, request, view

from global_values import *
from check_if_logged_in import check_if_logged_in

@get("/login")
@view("login.html")
def login_view():

    error = request.params.get("error")

    # get email from params to set as value in input 
    user_email = request.params.get("user_email")

    return dict(error=error, user_email=user_email, is_logged_in=check_if_logged_in())
