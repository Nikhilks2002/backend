from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    id: str
    email: str
    name: str

class PaymentCreate(BaseModel):
    id: str
    user_id: str
    amount: int
    currency: str
    status: Optional[str] = "pending"

class PaymentResponse(BaseModel):
    id: str
    user_id: str
    amount: int
    currency: str
    status: str
    created_at: Optional[str]
