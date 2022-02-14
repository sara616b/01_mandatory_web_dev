from bottle import redirect, request, post
import re
import uuid

# GLOBAL VALUES #############################
from global_values import REGEX_EMAIL, SESSIONS, USERS, TWEETS

##############################
@post("/signup")
def signup():
    # get the info from the form and validate the info
    errors = []
    form_inputs = {}

    # first name
    new_user_first_name = request.forms.get("new_user_first_name")
    if not new_user_first_name:
        errors.append("first-name-missing")
    else:
        form_inputs["first-name"] = new_user_first_name
    if len(new_user_first_name) < 2 or len(new_user_first_name) > 50:
        errors.append("first-name-length")

    # last name
    new_user_last_name = request.forms.get("new_user_last_name")
    if not new_user_last_name:
        errors.append("last-name-missing")
    else:
        form_inputs["last-name"] = new_user_last_name

    # email
    new_user_email = request.forms.get("new_user_email")
    if not new_user_email:
        errors.append("email-missing")
    elif not re.match(REGEX_EMAIL, new_user_email):
        errors.append("email-invalid")
    if not new_user_email == '':
        form_inputs["email"] = new_user_email

    # username
    new_user_username = request.forms.get("new_user_username")
    if not new_user_username:
        errors.append("username-missing")
    else:
        form_inputs["username"] = new_user_username

    # password
    new_user_password = request.forms.get("new_user_password")
    if not new_user_password:
        errors.append("password-missing")

    # potential error messages
    if not errors == []:
        error_string = f'{"=error&".join(errors)}=error'
        form_input_string = ''
        for value in form_inputs:
            form_input_string += f"&{value}={form_inputs[value]}"
        return redirect(f"/signup?{error_string}{form_input_string}")
    
    # append user to USERS
    new_user = {
        "first_name": new_user_first_name,
        "last_name": new_user_last_name,
        "email": new_user_email,
        "username": new_user_username,
        "password": new_user_password,
        "id": str(uuid.uuid4())
    }
    USERS.append(new_user)

    return redirect("/signup-success")
