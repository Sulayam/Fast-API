## hashing passwords
from passlib.context import CryptContext
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():

    @staticmethod
    def bcrypt(password: str):
        hashed_password = pwd_cxt.hash(password)
        return hashed_password

    @staticmethod
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)