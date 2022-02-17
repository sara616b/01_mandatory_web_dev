from bottle import get, request, redirect
from global_values import *

@get("/logout")
def logout():
    user_session_id = request.get_cookie("jwt", secret="secret")
    SESSIONS.remove(user_session_id)
    return redirect("/login")