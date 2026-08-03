
# main.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("API_KEY")  # Access the API key securely

if not api_key:
    raise RuntimeError("Missing API_KEY. Set it in your environment or .env file.")
if api_key:
    print("API_KEY found")
