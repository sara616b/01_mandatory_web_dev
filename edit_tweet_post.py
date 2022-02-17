from bottle import redirect, request, post
import time

from global_values import *

##############################
@post("/edit-tweet/<id>")
def edit_tweet_post(id):
    
    tweet_title = request.forms.get("new_tweet_title")
    if not tweet_title:
        print("No title")
    
    tweet_description = request.forms.get("new_tweet_description")
    if not tweet_description:
        print("No description")
        
    for index, tweet in enumerate(TWEETS):
        if tweet["id"] == id:
            tweet["title"] = tweet_title
            tweet["description"] = tweet_description
            tweet["time_edited"] = time.localtime()

    # return redirect(f"/edit-tweet/{id}?title={tweet_title}&description={tweet_description}")
    return redirect("/feed")
