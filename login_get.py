from bottle import get, view

# GLOBAL VALUES #############################
from global_values import REGEX_EMAIL, SESSIONS, USERS, TWEETS

##############################
@get("/login")
@view("login.html")
def login_view():
    return
