from fastapi import APIRouter
from . import schemas
router = APIRouter(
    prefix="/Kegan",
    tags=["Actors"]
)

@router.post("/")
def Kegan1(request: schemas.Test):
    return {"message1": request.message1, "message2": request.message2}