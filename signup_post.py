from bottle import redirect, request, post
import re

# GLOBAL VALUES #############################
from global_values import REGEX_EMAIL, SESSIONS, USERS, TWEETS

##############################
@post("/signup")
def signup():
    # get the info from the form and validate the info
    errors = []

    # first name
    new_user_first_name = request.forms.get("new_user_first_name")
    if not new_user_first_name:
        errors.append("first-name-missing")
    if len(new_user_first_name) < 2 or len(new_user_first_name) > 50:
        errors.append("first-name-length")

    # last name
    new_user_last_name = request.forms.get("new_user_last_name")
    if not new_user_last_name:
        errors.append("last-name-missing")

    # email
    new_user_email = request.forms.get("new_user_email")
    if not re.match(REGEX_EMAIL, new_user_email):
        errors.append("email-invalid")

    # username
    new_user_username = request.forms.get("new_user_username")

    # password
    new_user_password = request.forms.get("new_user_password")

    # potential error messages
    if not errors == []:
        error_string = f'{"=error&".join(errors)}=error'
        return redirect(f"/signup?{error_string}")
    
    # append user to USERS
    new_user = {
        "first_name": new_user_first_name,
        "last_name": new_user_last_name,
        "email": new_user_email,
        "username": new_user_username,
        "password": new_user_password,
    }
    USERS.append(new_user)
    print(USERS)

    return redirect("/signup-success")
