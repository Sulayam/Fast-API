from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models
from .. import hashing
from .. import database
get_db = database.get_db


def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = hashing.Hash.bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

def show_user_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not available")
    return user

def destroy_user(name: str, db: Session = Depends(get_db)):
    deleted_user = db.query(models.User).filter(models.User.name == name)
    if not deleted_user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {name}")
    deleted_user.delete(synchronize_session=False)
    db.commit()
    return f'deleted user with name: {name}'