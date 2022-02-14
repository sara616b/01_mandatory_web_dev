from bottle import get, redirect, view

# GLOBAL VALUES #############################
from global_values import *
from check_if_logged_in import check_if_logged_in

##############################
@get("/new-tweet")
@view("new_tweet.html")
def index_view():
    if not check_if_logged_in():
        return redirect("/login")
    
    return dict(is_logged_in=check_if_logged_in())
