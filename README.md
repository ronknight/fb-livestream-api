<h1 align="center">📺 <a href="#">Facebook Livestream Status Checker</a></h1>

<h4 align="center">🔧 A Flask-based web application to check the status of Facebook livestreams and scheduled broadcasts.</h4>

<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://github.com/ronknight/ronknight/stargazers"><img src="https://img.shields.io/github/stars/BEPb/BEPb.svg?logo=github"></a>
<a href="https://github.com/ronknight/ronknight/network/members"><img src="https://img.shields.io/github/forks/BEPb/BEPb.svg?color=blue&logo=github"></a>
<a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
<a href="#"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="#LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Love-1f425f.svg"></a>
<a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-Ronknight%20-%20red"></a>
</p>

---

## 🌟 Project Overview
This project is a Flask-based application designed to monitor Facebook livestreams in real-time and notify users if:
- A livestream is currently active (`Live`).
- A livestream is scheduled to start soon (`Scheduled`).
- No livestreams are currently happening (`Offline`).

It utilizes the **Facebook Graph API** to fetch livestream statuses and implements a schedule-based system for anticipating upcoming streams.

---

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#api-endpoints">API Endpoints</a> •
  <a href="#configuration">Configuration</a> •
  <a href="#visualization">Visualization</a> •
  <a href="#disclaimer">Disclaimer</a>
</p>

---

## ✨ Features
- **Livestream Monitoring**: Automatically checks if a livestream is currently active on a Facebook Page.
- **Schedule Detection**: Determines if the current time is near a predefined livestream schedule.
- **CORS Support**: Configured for Cross-Origin Resource Sharing to allow external API requests.
- **Health Check**: A `/health` endpoint to verify application health.
- **Error Handling**: Robust logging and error management for API calls and application routes.
- **Placeholder Image**: Displays a default image if no livestream is available.

---

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and provide the following:
   ```env
   FLASK_APP_SECRET_KEY=your_secret_key
   FACEBOOK_APP_ID=your_facebook_app_id
   FACEBOOK_PAGE_ID=your_facebook_page_id
   FACEBOOK_CLIENT_TOKEN=your_facebook_client_token
   ACCESS_TOKEN=your_facebook_access_token
   CORS_ORIGINS=http://example.com,http://localhost:3000
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the application at:
   - `http://127.0.0.1:5000` (default Flask development server)

---

## 🛠 Usage

### Local Development
- Ensure the `.env` file is correctly set up with Facebook API credentials.
- The app will fetch the livestream status based on the `/check-livestream` endpoint.

### Deployment
- Update `ssl_context` in `app.run()` to include the proper paths for the SSL certificate and key files.

---

## 📡 API Endpoints

| Method | Endpoint            | Description                                      |
|--------|---------------------|--------------------------------------------------|
| GET    | `/`                 | Renders the home page or a default message.      |
| GET    | `/check-livestream` | Checks if a livestream is currently live, scheduled, or offline. |
| GET    | `/health`           | Health check to verify if the server is running. |

---

## ⚙️ Configuration

- **Livestream Schedule**:
  You can modify the livestream schedule in the `SCHEDULE` list within the code:
  ```python
  SCHEDULE = [
      {"day": "Wednesday", "hour": 19, "minute": 0},
      {"day": "Sunday", "hour": 10, "minute": 0},
      {"day": "Sunday", "hour": 17, "minute": 0},
  ]
  ```
- **CORS Origins**:
  Update allowed origins in the `.env` file:
  ```env
  CORS_ORIGINS=http://example.com,http://localhost:3000
  ```

---

## 📊 Visualization

```mermaid
graph TD
A[User] -->|HTTP Request| B[Flask App]
B --> C[/check-livestream Endpoint]
C -->|Facebook Graph API Request| D[Facebook Livestream Status]
D -->|Returns JSON| C
C -->|Livestream Details| E[User Interface]
```

---

## ⚠️ Disclaimer

This project interacts with the Facebook API. Ensure you have appropriate permissions and comply with Facebook's API usage policies. The project requires sensitive credentials stored in a `.env` file; handle these carefully to prevent unauthorized access.