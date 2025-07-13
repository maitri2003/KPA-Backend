from pydantic import BaseModel

class UserLogin(BaseModel):
    phone_number: str
    password: str

class LoginResponse(BaseModel):
    message: str
    user_id: int
