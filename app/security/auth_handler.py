import time
import jwt
from typing import Dict
from decouple import config
from jwt.exceptions import PyJWKError


JWT_SECRET_KEY = config("secret")
JWT_ALGORITHM = config("algorithm")

def token_response(token: str) -> Dict[str, str]:
    return {"access_token": token, "token_type": "bearer"}  

def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "exp": time.time() + 1800,  # Token válido por 30 minutos
        "role": "user"
    }
    token = jwt.encode(
        payload, 
        JWT_SECRET_KEY, 
        algorithm=JWT_ALGORITHM
        )

    return token_response(token)

def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token, 
            JWT_SECRET_KEY, 
            algorithms=[JWT_ALGORITHM]
            )
        return decoded_token 
    except jwt.ExpiredSignatureError:
        return None
    except PyJWKError:
        return None
