import hashlib
import datetime
import jwt
from fastapi import HTTPException, Request


SECRET = "TSTNatMamah"

def get_hash(string):
    if (type(string) is str):
        message = string.encode()
        return hashlib.sha256(message).hexdigest()
    else:
        return None

def encode_token(email):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days = 3),
            'iat': datetime.datetime.utcnow(),
            'email': email
        }
        return jwt.encode(
            payload,
            SECRET
        )
    except Exception as e:
        return e

def authorize(request: Request):
    try:
        token = request.headers.get('Authorization').split(' ')[1]
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload.get('email')
    except:
        raise HTTPException(status_code = 401, detail = "Invalid token, try login again")
