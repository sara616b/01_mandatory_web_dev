from bottle import get, redirect, request, view

from global_values import *
from check_if_logged_in import check_if_logged_in

@get("/edit-tweet/<id>")
@view("edit_tweet.html")
def edit_tweet_view(id):
    if not check_if_logged_in():
        return redirect("/login")
    
    tweet_to_edit = {}
    error = request.params.get("error")
    
    # find tweet to edit based on id in url
    for index, tweet in enumerate(TWEETS):
        if tweet["id"] == id:
            tweet_to_edit = tweet
    
    return dict(is_logged_in=check_if_logged_in(), tweet=tweet_to_edit, error=error)
