from bottle import get, request, view

# GLOBAL VALUES #############################
from global_values import REGEX_EMAIL, SESSIONS, USERS, TWEETS

##############################
@get("/login")
@view("login.html")
def login_view():
    error = request.params.get("error")
    user_email = request.forms.get("user_email")
    return dict(error=error, user_email=user_email)
