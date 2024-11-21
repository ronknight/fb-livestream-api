import os
import datetime
import logging
from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
from flask_cors import CORS
import requests

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Secret key for Flask app
app.secret_key = os.getenv("FLASK_APP_SECRET_KEY")

# Retrieve Facebook API credentials
FACEBOOK_APP_ID = os.getenv("FACEBOOK_APP_ID")
FACEBOOK_PAGE_ID = os.getenv("FACEBOOK_PAGE_ID")
FACEBOOK_CLIENT_TOKEN = os.getenv("FACEBOOK_CLIENT_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# Validate critical environment variables
if not FACEBOOK_APP_ID or not FACEBOOK_CLIENT_TOKEN or not ACCESS_TOKEN or not FACEBOOK_PAGE_ID:
    raise ValueError("Critical Facebook credentials are missing from the .env file")

# Configure CORS (Cross-Origin Resource Sharing)
cors_origins = os.getenv("CORS_ORIGINS", "").split(",")
CORS(app, resources={r"/*": {"origins": cors_origins}})

# URL for the background image if no livestream
NO_LIVESTREAM_IMAGE = "https://gbclongbeach.org/wp-content/uploads/2024/11/placeholder-background.png"

# Livestream schedule (in UTC)
SCHEDULE = [
    {"day": "Wednesday", "hour": 19, "minute": 0},
    {"day": "Sunday", "hour": 10, "minute": 0},
    {"day": "Sunday", "hour": 17, "minute": 0},
]

# Function to check if there is an ongoing livestream on Facebook
def is_live():
    url = f'https://graph.facebook.com/v17.0/{FACEBOOK_PAGE_ID}/live_videos?access_token={ACCESS_TOKEN}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        live_videos = response.json().get('data', [])
        for video in live_videos:
            if video.get('status') == 'LIVE':
                return True
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error checking Facebook livestream: {e}")
    return False

# Function to check if it is near a scheduled livestream time
def is_scheduled():
    current_time = datetime.datetime.utcnow()
    current_day = current_time.strftime('%A')
    for schedule in SCHEDULE:
        if current_day == schedule["day"]:
            livestream_time = datetime.datetime(
                current_time.year, current_time.month, current_time.day,
                schedule["hour"], schedule["minute"]
            )
            time_difference = (livestream_time - current_time).total_seconds() / 60
            if 0 <= time_difference <= 10:  # Check if within 10 minutes before scheduled time
                return True
    return False

# API endpoint to check livestream status
@app.route('/check-livestream', methods=['GET'])
def check_livestream():
    try:
        if is_live():
            return jsonify({"status": "Live", "message": "A livestream is happening now!"}), 200
        elif is_scheduled():
            return jsonify({"status": "Scheduled", "message": "A livestream is scheduled to start soon."}), 200
        else:
            return jsonify({
                "status": "Offline",
                "message": "No livestream at the moment.",
                "background": NO_LIVESTREAM_IMAGE
            }), 200
    except Exception as e:
        app.logger.error(f"Error in /check-livestream endpoint: {e}")
        return jsonify({"status": "Error", "message": "An internal server error occurred."}), 500

# Default route to serve a basic template or message
@app.route('/')
def home():
    try:
        return render_template('index.html')  # Adjust template as needed
    except Exception as e:
        app.logger.error(f"Error in root route: {e}")
        return jsonify({"status": "Error", "message": "An internal server error occurred."}), 500

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # Enable SSL for Flask
    app.run(
        host="0.0.0.0",
        port=5000,
        ssl_context=(
            '/home/pinoyits/var/cpanel/ssl/apache_tls/pinoyitsolution.com/cert.pem',  # Certificate file
            '/home/pinoyits/var/cpanel/ssl/apache_tls/pinoyitsolution.com/key.pem'    # Private key file
            #'cert.pem',  # SSL Certificate
            #'key.pem'   # SSL Private Key
        )
    )
