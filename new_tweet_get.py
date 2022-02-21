from bottle import get, redirect, request, view

from global_values import *
from check_if_logged_in import check_if_logged_in

@get("/new-tweet")
@view("new_tweet.html")
def index_view():
    if not check_if_logged_in():
        return redirect("/login")
    
    error = request.params.get("error")
    
    return dict(is_logged_in=check_if_logged_in(), error=error)
