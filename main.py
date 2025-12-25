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

# List all users
@app.get("/users")
def get_users():
    result = supabase.table("users").select("*").execute()
    return {"users": result.data}

# Add a payment
@app.post("/payments")
def add_payment(user_id: str, amount: int, payment_name: str = "Default Payment"):
    result = supabase.table("payments").insert({
        "user_id": user_id,
        "amount": amount,
        "currency": "USD",
        "status": "pending",
        "payment_name": payment_name
    }).execute()
    return {"message": "Payment added", "payment": result.data}

# Fetch complete user data by email
@app.get("/user-data")
def get_user_data(email: str = Query(...)):
    # 1️⃣ Get user info by email
    user_result = supabase.table("users").select("*").eq("email", email).execute()
    if not user_result.data:
        return {"error": "No user found with this email"}

    user = user_result.data[0]

    # 2️⃣ Get all payments for this user
    payments_result = supabase.table("payments").select("*").eq("user_id", user["id"]).execute()

    return {
        "user": {
            "username": user.get("username"),
            "email": user.get("email"),
            "account_created_at": user.get("created_at"),
            "account_type": user.get("account_type", "N/A"),  # optional if you store
            "other_details": user.get("other_details", {})    # any extra fields
        },
        "payments": [
            {
                "payment_name": p.get("payment_name", "N/A"),
                "amount": p.get("amount"),
                "currency": p.get("currency"),
                "status": p.get("status"),
                "created_at": p.get("created_at")
            } for p in payments_result.data
        ]
    }
