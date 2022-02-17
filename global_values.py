import uuid
import time

SESSIONS = []
TWEETS = [{
        "id": str(uuid.uuid4()),
        "user_id": str(uuid.uuid4()),
        "first_name": "Name Here",
        "username": "test",
        "title": "Pretty title",
        "description": "Funny tweet, haha!",
        "time_posted": time.localtime(),
        "time_edited": None,
    }]
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