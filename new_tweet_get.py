from bottle import get, redirect, request, view

from global_values import *
from check_if_logged_in import check_if_logged_in

@get("/new-tweet")
@view("new_tweet.html")
def index_view():
    if not check_if_logged_in():
        return redirect("/login")
    
    description = request.params.get("description")
    title = request.params.get("title")
    error = request.params.get("error")
    
    return dict(is_logged_in=check_if_logged_in(), description=description, title=title, error=error)
