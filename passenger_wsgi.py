import os
from app import app  # Import your Flask app object

# Ensure the environment variables from .env are loaded
from dotenv import load_dotenv
load_dotenv()

# Define the WSGI application object
application = app
