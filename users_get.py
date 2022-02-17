from bottle import get, view

from global_values import USERS
from check_if_logged_in import check_if_logged_in

##############################
@get("/users")
@view("users.html")
def users_view():
    if not check_if_logged_in():
        return redirect("/login")
    return dict(users=USERS, is_logged_in=check_if_logged_in())

