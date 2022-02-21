from bottle import request
import jwt
from jwt.exceptions import InvalidSignatureError

from global_values import *

def check_if_logged_in():
    is_logged_in = False
    
    # if the jwt cookie is in SESSIONS and is valid set is_logged_in to value from user_information (True) else print error
    if request.get_cookie("jwt", secret="secret") and request.get_cookie("jwt", secret="secret") in SESSIONS:
        try:
            user_information = jwt.decode(request.get_cookie("jwt", secret="secret"), JWT_KEY, algorithms=["HS256"]) or 'Nothing'
            is_logged_in = user_information["is_logged_in"]
        except InvalidSignatureError as error:
            print(f"Invalid signature error: {error}")

    return is_logged_in
