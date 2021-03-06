from bottle import get, run, static_file

from global_values import REGEX_EMAIL, SESSIONS, USERS, TWEETS

# STYLESHEET #############################
@get("/app.css")
def style():
    return static_file("app.css", root=".")

# IMPORTING MODULES #############################
import index_get
import users_get
import signup_get
import signup_post
import signup_success_get
import login_get
import login_post
import logout_get
import new_tweet_get
import new_tweet_post
import dashboard_get
import delete_tweet_post
import edit_tweet_get
import edit_tweet_post

run(host="127.0.0.1", port="4444", reloader=True, debug=True, server="paste")