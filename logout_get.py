from bottle import get, run, static_file, view, post, request, response, redirect
from global_values import *

# LOGOUT GET #############################
@get("/logout")
def logout():
    user_session_id = request.get_cookie("jwt", secret="secret")
    SESSIONS.remove(user_session_id)
    return redirect("/login")