from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access environment variables
PASSWORD = os.getenv("PASSWORD")