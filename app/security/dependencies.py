from fastapi import HTTPException, Request, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .auth_handler import decode_jwt
from models.user import User

security_schme = HTTPBearer

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security_schme)) -> User:
        token = credentials.credentials
        
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        
        
