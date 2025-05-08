from db import user_collection
from utils.hash import hash_password, verify_password
from bson.objectid import ObjectId


def find_user(username: str):
    return user_collection.find_one({"username": username})

def register_user(username: str, password: str):
    if find_user(username):
        return False
    user_collection.insert_one({
        "username": username,
        "hashed_password": hash_password(password)
    })
    return True

def authenticate_user(username: str, password: str):
    user = find_user(username)
    if not user:
        return False
    return verify_password(password, user["hashed_password"])
