from bottle import get, redirect, request, view
import jwt

from global_values import *
from check_if_logged_in import check_if_logged_in

@get("/home")
@view("home.html")
def home_view():
    user_session_jwt = request.get_cookie("jwt", secret="secret")
    if user_session_jwt not in SESSIONS:
        return redirect("/login")
    user_information = jwt.decode(user_session_jwt, JWT_KEY, algorithms=["HS256"])
    user_email = user_information["email"]
    user_first_name = user_information["first_name"]
    return dict(user_email=user_email, user_first_name=user_first_name, is_logged_in=check_if_logged_in())
