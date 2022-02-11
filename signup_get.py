from bottle import get, view

# GLOBAL VALUES #############################
from global_values import REGEX_EMAIL, SESSIONS, USERS, TWEETS

##############################
@get("/signup")
@view("signup.html")
def signup_view():
    return
