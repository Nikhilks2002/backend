from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine and test connection
try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("Connected successfully!")
    connection.close()
except Exception as e:
    print("Connection failed:", e)
