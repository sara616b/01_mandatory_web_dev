from bottle import get, redirect, request, view
import jwt

from global_values import *
from check_if_logged_in import check_if_logged_in

@get("/dashboard")
@view("dashboard.html")
def dashboard_view():
    if not check_if_logged_in():
        return redirect("/login")
    
    # get user information to connect with own tweets and allow the user to edit or delete these
    user_session_jwt = request.get_cookie("jwt", secret="secret")
    if user_session_jwt not in SESSIONS:
        return redirect("/login")
    user_information = jwt.decode(user_session_jwt, JWT_KEY, algorithms=["HS256"])
    user_id = user_information["id"]
    
    return dict(tweets=TWEETS, user_id=user_id, is_logged_in=check_if_logged_in())

