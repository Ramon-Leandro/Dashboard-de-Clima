<div align="center">

# 🌤️ Weather Dashboard

**A full-stack weather monitoring app with real-time search and persistent search history.**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-Build-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vitejs.dev/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-API-EB6E4B?style=for-the-badge)](https://openweathermap.org/api)

</div>

---

## 📌 About

Weather Dashboard is a full-stack application that lets users search for real-time weather conditions in any city around the world. Every search is automatically saved to a SQL database, giving users an organized history of all their recent lookups.

The project demonstrates a clear client-server architecture: a **React + Vite** frontend communicates with a **Flask** REST API, which fetches live data from OpenWeatherMap and persists queries using **SQLAlchemy + SQLite**.

---

## ✨ Features

- 🔍 **City Search** — Look up current weather for any city in real time
- 📊 **Search History** — All queries are saved and displayed in an organized list
- ☁️ **Live Weather Data** — Temperature, humidity, conditions, and more via OpenWeatherMap
- 🗄️ **Data Persistence** — History survives page reloads via SQLite database
- 🔗 **REST API** — Clean JSON API powering the frontend
- 🌐 **CORS Configured** — Secure cross-origin communication between frontend and backend

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend Language | JavaScript |
| Frontend Framework | React.js + Vite |
| Backend Language | Python 3 |
| Backend Framework | Flask |
| ORM | SQLAlchemy |
| Database | SQLite |
| External API | OpenWeatherMap |
| Cross-Origin | Flask-CORS |

---

## 📁 Project Structure

```
Dashboard-de-Clima/
├── app.py               # Flask backend — routes and API logic
├── frontend/
│   ├── src/
│   │   ├── App.jsx      # Main React component
│   │   └── ...          # Other components
│   ├── package.json
│   └── vite.config.js
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Node.js and npm
- An [OpenWeatherMap API key](https://openweathermap.org/api) (free tier is enough)

### Step 1 — Backend Setup

```bash
# 1. Clone the repository
git clone https://github.com/Ramon-Leandro/Dashboard-de-Clima.git
cd Dashboard-de-Clima

# 2. Install Python dependencies
pip install flask flask-sqlalchemy flask-cors requests

# 3. Add your OpenWeatherMap API key
# Open app.py and set your key in the API_KEY variable

# 4. Start the Flask server
python app.py
```

The API will run at `http://localhost:5000`.

### Step 2 — Frontend Setup

```bash
# In a new terminal, navigate to the frontend folder
cd frontend

# Install Node.js dependencies
npm install

# Start the Vite dev server
npm run dev
```

The app will be available at `http://localhost:5173`.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/weather?city={city}` | Fetch current weather for a city |
| `GET` | `/history` | Retrieve all past searches |

### Example — Fetch Weather

**Request:**
```http
GET /weather?city=São Paulo
```

**Response `200 OK`:**
```json
{
  "city": "São Paulo",
  "temperature": 22.5,
  "humidity": 68,
  "description": "few clouds",
  "icon": "02d"
}
```

---

## 🖼️ Screenshots

<details>
<summary>Click to expand</summary>

**Main Interface — After a Search**
![Weather Dashboard in operation]({745825B0-3589-4378-968B-D511A531D549}.png)

**Initial State — Before Any Search**
![Initial dashboard without searches]({ED46C13A-CA08-4FFB-BE70-ABB29A5293FB}.png)

**Backend API Response (JSON)**
![API response in JSON format]({3CDB199E-D8F0-48A7-9780-34C9022B861F}.png)

</details>

---

## 🧠 Concepts Demonstrated

This project was built to consolidate key full-stack engineering concepts:

| Concept | Implementation |
|---|---|
| Client-Server Architecture | React frontend ↔ Flask backend via REST |
| External API Integration | OpenWeatherMap for live weather data |
| Data Persistence | SQLAlchemy ORM managing SQLite queries |
| Cross-Origin Resource Sharing | Flask-CORS allowing frontend ↔ backend communication |
| JSON Communication | Structured API responses consumed by React |

---

## 🔧 Environment Variables

| Variable | Description |
|---|---|
| `API_KEY` | Your OpenWeatherMap API key (set in `app.py`) |

---

## 🎓 About This Project

This project was developed for educational purposes as a practical exercise in full-stack development, covering:

- Consuming third-party REST APIs with Python's `requests` library
- Building a REST API backend with **Flask**
- Managing a SQL database through an ORM (**SQLAlchemy**)
- Integrating a **React** frontend with a Python backend
- Handling asynchronous communication between client and server

---

## 👤 Author

**Ramon Leandro**

[![GitHub](https://img.shields.io/badge/GitHub-Ramon--Leandro-181717?style=flat&logo=github)](https://github.com/Ramon-Leandro)
