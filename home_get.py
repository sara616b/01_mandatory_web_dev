from bottle import get, view

# GLOBAL VALUES #############################
from global_values import REGEX_EMAIL, SESSIONS, USERS, TWEETS

##############################
@get("/")
@view("index.html")
def home_view():
    return
