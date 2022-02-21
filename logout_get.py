from bottle import get, request, redirect
from global_values import *

@get("/logout")
def logout():

    # remove cookie from session to log out the user
    user_session_id = request.get_cookie("jwt", secret="secret")
    SESSIONS.remove(user_session_id)
    
    return redirect("/login")