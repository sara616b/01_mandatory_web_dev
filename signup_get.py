from bottle import get, request, view

from global_values import *
from check_if_logged_in import check_if_logged_in

@get("/signup")
@view("signup.html")
def signup_view():

    # get errors to display in signup.html
    # TODO - smarter way to do this x_X
    errors = {}
    errors["first_name_missing"] = request.params.get("first-name-missing") if request.params.get("first-name-missing") else 'no-error'
    errors["first_name_length"] = request.params.get("first-name-length") if request.params.get("first-name-length") else 'no-error'
    errors["last_name_missing"] = request.params.get("last-name-missing") if request.params.get("last-name-missing") else 'no-error'
    errors["email_missing"] = request.params.get("email-missing") if request.params.get("email-missing") else 'no-error'
    errors["email_invalid"] = request.params.get("email-invalid") if request.params.get("email-invalid") else 'no-error'
    errors["user_exists_email"] = request.params.get("user-exists-email") if request.params.get("user-exists-email") else 'no-error'
    errors["username_missing"] = request.params.get("username-missing") if request.params.get("username-missing") else 'no-error'
    errors["password_missing"] = request.params.get("password-missing") if request.params.get("password-missing") else 'no-error'
    errors["password_short"] = request.params.get("password-short") if request.params.get("password-short") else 'no-error'
    errors["user_exists_username"] = request.params.get("user-exists-username") if request.params.get("user-exists-username") else 'no-error'

    # get values in form from url so they're remembered after reload
    form_values = {}
    form_values["user_first_name"] = request.params.get("first-name") 
    form_values["user_last_name"] = request.params.get("last-name")
    form_values["user_email"] = request.params.get("email")
    form_values["user_username"] = request.params.get("username")

    values = form_values | errors | dict(is_logged_in=check_if_logged_in())
    
    return values
