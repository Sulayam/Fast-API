from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas
from sqlalchemy.orm import Session
from .. database import get_db
from .. repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    result = user.create_user(request, db)
    return result

@router.get('/',status_code=status.HTTP_200_OK,tags=["Users"], response_model=List[schemas.ShowUser])
def all_users(db: Session = Depends(get_db)):
    return user.all_users(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show_user_id(id: int, db: Session = Depends(get_db)):
    return user.show_user_id(id, db)

@router.delete('/{name}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_user(name: str, db: Session = Depends(get_db)):
    return user.destroy_user(name, db)