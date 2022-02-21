from bottle import redirect, post

from global_values import *

@post("/delete-tweet/<id>")
def delete_tweet_post(id):

    # find tweet to delete based on id i url
    for index, tweet in enumerate(TWEETS):
        if tweet["id"] == id:
            TWEETS.pop(index)

    return redirect("/dashboard")
