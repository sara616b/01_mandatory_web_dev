from bottle import redirect, response, request, post
import re
import jwt

from global_values import JWT_KEY, REGEX_EMAIL, SESSIONS, USERS


@post("/login")
def login_post():
    user_email = request.forms.get("user_email")
    if not user_email:
        return redirect("/login?error=user_email")
    if not re.match(REGEX_EMAIL, user_email):
        return redirect("/login?error=user_email")
    if not request.forms.get("user_password"):
        return redirect(f"/login?error=user_password&user_email={user_email}")
    for user in USERS:
        if user["email"] == user_email and user["password"] == request.forms.get("user_password"):
            user["is_logged_in"] = True
            user_session_jwt = jwt.encode(user, JWT_KEY, algorithm="HS256")
            SESSIONS.append(user_session_jwt)
            response.set_cookie("jwt", user_session_jwt, secret="secret")
            return redirect("/feed")
    return redirect("/login?error=no_user")
