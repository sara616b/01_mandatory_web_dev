from bottle import get, post, run, static_file, view


# GLOBAL VALUES #############################


# STYLESHEET #############################
@get("/app.css")
def style():
    return static_file("app.css", root=".")

##############################
@get("/")
@view("index.html")
def home_view():
    return

run(host="127.0.0.1", port="4444", reloader=True, debug=True, server="paste")