from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. database import get_db
from .. import schemas, models
from .. hashing import Hash



router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    print("aaaaaaaa")
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Credentials"
        )
    print("bbbbbb")
    # hashing.Hash.bcrypt(request.password)
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect Password"
        )
    print("cccccc")
    return user