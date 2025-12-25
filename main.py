from fastapi import FastAPI, Query
from database import supabase

app = FastAPI(
    title="Payment API with Supabase",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
def root():
    return {"message": "Backend is running successfully"}

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

# Updated endpoint
@app.get("/payments")
def get_user_payments(user_id: str = Query(None)):
    query = supabase.table("payments").select("*")
    if user_id:
        query = query.eq("user_id", user_id)
    result = query.execute()
    return {"payments": result.data}
