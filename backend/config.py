import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables with default fallbacks
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
YOUR_CELL_PHONE_NUMBER = os.getenv("YOUR_CELL_PHONE_NUMBER")

# Add any other API keys here
X_API_KEY = os.getenv("X_API_KEY")
X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")