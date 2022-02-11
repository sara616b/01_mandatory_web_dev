from bottle import get, view

# GLOBAL VALUES #############################
from global_values import REGEX_EMAIL, SESSIONS, USERS, TWEETS

##############################
@get("/signup-success")
@view("signup_success.html")
def signup_success_view():
    return
