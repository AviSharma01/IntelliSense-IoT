from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session

from database.queries import get_user_by_username
from security import hash_password, verify_password


security = HTTPBasic()


def get_current_user(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = get_user_by_username(db, username=credentials.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    if not verify_password(credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    return user


def is_admin(user = Depends(get_current_user)):
    if not user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is not an administrator")
    return True


def create_user(db: Session, username: str, password: str, email: str, is_admin: bool = False):
    hashed_password = hash_password(password)
    user = get_user_by_username(db, username=username)
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already taken")
    db.execute(
        "INSERT INTO users (username, password, email, is_admin) VALUES (:username, :password, :email, :is_admin)",
        {"username": username, "password": hashed_password, "email": email, "is_admin": is_admin}
    )
    db.commit()
    return {"username": username, "email": email, "is_admin": is_admin}


def delete_user(db: Session, username: str):
    user = get_user_by_username(db, username=username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.execute("DELETE FROM users WHERE username = :username", {"username": username})
    db.commit()
    return {"message": "User deleted"}
