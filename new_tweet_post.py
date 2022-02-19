from bottle import redirect, request, post
import uuid
import jwt
import time

from global_values import *

@post("/new-tweet")
def new_tweet_post():
    
    form_inputs = {}
    
    new_tweet_title = request.forms.get("new_tweet_title")
    if not new_tweet_title:
        print("No title")
    else:
        form_inputs["title"] = new_tweet_title
    
    new_tweet_description = request.forms.get("new_tweet_description")
    if not new_tweet_description:
        print("No description")
    else:
        form_inputs["description"] = new_tweet_description
        
    if not new_tweet_title:
        if not new_tweet_description:
            return redirect("/new-tweet?error=empty" + "" if not new_tweet_description else f"description={new_tweet_description}" + "" if not new_tweet_title else f"description={new_tweet_title}")
    
    user_session_jwt = request.get_cookie("jwt", secret="secret")
    if user_session_jwt not in SESSIONS:
        return redirect("/login")
    user_information = jwt.decode(user_session_jwt, JWT_KEY, algorithms=["HS256"])
    user_username = user_information["username"]
    user_first_name = user_information["first_name"]
    user_id = user_information["id"]
    
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
    print(new_tweet)

    return redirect("/feed")
