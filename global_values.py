import uuid

SESSIONS = []
TWEETS = []
USERS = [{
        "first_name": "Sarah",
        "last_name": "Frederiksen",
        "email": "sarah@mail.com",
        "username": "sarah",
        "password": "123",
        "id": str(uuid.uuid4())
    }]

JWT_KEY = f"{str(uuid.uuid4())}-{str(uuid.uuid4())}-{str(uuid.uuid4())}"
REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'