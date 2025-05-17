from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas
from .. import models
from .. database import get_db
from sqlalchemy.orm import Session
from .. repository import blog
from .. oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db:Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create(request, db)

@router.get('/', tags=["Blogs"])
def all_blogs(db: Session= Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.all_blogs(db)

@router.get("/{id}", status_code=200)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.show(id, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.destroy(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.update(id, request, db)