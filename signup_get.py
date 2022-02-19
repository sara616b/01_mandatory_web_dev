from bottle import get, request, view

from global_values import *
from check_if_logged_in import check_if_logged_in

@get("/signup")
@view("signup.html")
def signup_view():
    errors = {}
    errors["first_name_missing"] = request.params.get("first-name-missing") if request.params.get("first-name-missing") else 'no-error'
    errors["first_name_length"] = request.params.get("first-name-length")
    errors["last_name_missing"] = request.params.get("last-name-missing")
    errors["email_missing"] = request.params.get("email-missing")
    errors["email_invalid"] = request.params.get("email-invalid")
    errors["user_exists_email"] = request.params.get("user-exists-email")
    errors["username_missing"] = request.params.get("username-missing")
    errors["password_missing"] = request.params.get("password-missing")
    errors["password_short"] = request.params.get("password-short")
    errors["user_exists_username"] = request.params.get("user-exists-username")

    form_values = {}
    form_values["user_first_name"] = request.params.get("first-name") 
    form_values["user_last_name"] = request.params.get("last-name")
    form_values["user_email"] = request.params.get("email")
    form_values["user_username"] = request.params.get("username")

    values = form_values | errors | dict(is_logged_in=check_if_logged_in())
    
    return values
