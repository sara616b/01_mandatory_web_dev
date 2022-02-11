from bottle import get, post, run, static_file, view

# GLOBAL VALUES #############################
from global_values import REGEX_EMAIL, SESSIONS, USERS, TWEETS

# STYLESHEET #############################
@get("/app.css")
def style():
    return static_file("app.css", root=".")

# GET VIEWS #############################
import home_get
import users_get
import signup_get
import login_get

run(host="127.0.0.1", port="4444", reloader=True, debug=True, server="paste")