from bottle import get, request, view

# GLOBAL VALUES #############################
from global_values import REGEX_EMAIL, SESSIONS, USERS, TWEETS

##############################
@get("/signup")
@view("signup.html")
def signup_view():
    errors = {}
    errors["first_name_missing"] = request.params.get("first-name-missing")
    errors["first_name_length"] = request.params.get("first-name-length")
    errors["last_name_missing"] = request.params.get("last-name-missing")
    errors["email_invalid"] = request.params.get("email-invalid")

    # TODO - validate email and password
    return errors
