from bottle import get, view

# GLOBAL VALUES #############################
from global_values import REGEX_EMAIL, SESSIONS, USERS, TWEETS

##############################
@get("/users")
@view("users.html")
def users_view():
    return
