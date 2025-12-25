from fastapi import FastAPI
from database import supabase

app = FastAPI(title="Payment API with Supabase")

@app.get("/users")
def get_users():
    result = supabase.table("users").select("*").execute()
    return {"users": result.data}

@app.post("/payments")
def add_payment(user_id: str, amount: int):
    result = supabase.table("payments").insert({
        "user_id": user_id,
        "amount": amount,
        "currency": "USD",
        "status": "pending"
    }).execute()
    return {"message": "Payment added", "payment": result.data}

@app.get("/payments")
def get_payments():
    result = supabase.table("payments").select("*").execute()
    return {"payments": result.data}
