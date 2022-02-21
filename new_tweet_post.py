from bottle import redirect, request, post
import uuid
import jwt
import time

from check_if_logged_in import check_if_logged_in
from global_values import *

@post("/new-tweet")
def new_tweet_post():
    if not check_if_logged_in():
        return redirect("/login")
    
    # title
    new_tweet_title = request.forms.get("new_tweet_title")
    
    # description
    new_tweet_description = request.forms.get("new_tweet_description")
        
    # can't post empty tweet without either title or description
    if not new_tweet_title:
        if not new_tweet_description:
            return redirect("/new-tweet?error=empty")
    
    # decode jwt cookie to get user information for tweet
    user_information = jwt.decode(request.get_cookie("jwt", secret="secret"), JWT_KEY, algorithms=["HS256"])
    user_username = user_information["username"]
    user_first_name = user_information["first_name"]
    user_id = user_information["id"]
    
    # append new tweet with values
    new_tweet = {
        "id": str(uuid.uuid4()),
        "user_id": user_id,
        "first_name": user_first_name,
        "username": user_username,
        "title": new_tweet_title,
        "description": new_tweet_description,
        "time_posted": time.localtime(),
        "time_edited": None,
    }
    TWEETS.append(new_tweet)

    return redirect("/dashboard")
