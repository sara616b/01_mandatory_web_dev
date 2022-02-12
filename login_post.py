from bottle import redirect, response, request, post
import re
import uuid
import time
import jwt

# GLOBAL VALUES #############################
from global_values import REGEX_EMAIL, SESSIONS, USERS, TWEETS

jwt_key = f"{str(uuid.uuid4())}-{str(uuid.uuid4())}-{str(uuid.uuid4())}"

# LOGIN POST #############################
@post("/login")
def login_post():
    #VALIDATION!
    user_email = request.forms.get("user_email")
    if not user_email:
        return redirect("/login?error=user_email")
    if not re.match(REGEX_EMAIL, user_email):
        return redirect("/login?error=user_email")
    if not request.forms.get("user_password"):
        return redirect(f"/login?error=user_password&user_email={user_email}")
    if len(request.forms.get("user_password")) < 6 or len(request.forms.get("user_password")) > 50:
        return redirect(f"/login?error=user_password&user_email={user_email}")
    # check that it's right
    for user in USERS:
        if user["email"] == user_email and user["password"] == request.forms.get("user_password"):
            # SUCCESS
            user_session_jwt = jwt.encode(user, jwt_key, algorithm="HS256")
            SESSIONS.append(user_session_jwt)
            # loop through real user database to find information
            response.set_cookie("jwt", user_session_jwt, secret="secret")
            return redirect("/admin")
    return redirect("/login?error=no_user")
