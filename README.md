# CivicSense AI 🏙️🧠

*An autonomous AI agent for proactive civic issue management, built for the Hacktivism II hackathon.*

[![Hacktivism II](https://img.shields.io/badge/Hackathon-Hacktivism%20II-blueviolet)](https://hacktivism-2.devpost.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18-61DAFB?logo=react)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?logo=fastapi)](https://fastapi.tiangolo.com/)

---

## 💡 Inspiration

Municipal 311 systems are fundamentally **reactive**. They rely on citizens to report issues like potholes, broken streetlights, or power outages. This leads to delays, inefficient resource allocation, and a diminished quality of life. We asked: *Can we build a system that finds and flags these issues proactively, before they're even reported?*

**CivicSense AI** is our answer. It's a digital watchdog that autonomously monitors a city's real-time data streams to identify, prioritize, and dispatch civic issues, helping city management become **proactive**.

## ✨ What It Does

CivicSense AI is a full-stack application that:
1.  **Ingests Data** in real-time from multiple sources, including public APIs (like the Twitter/X API) and municipal data feeds (simulated 311 reports).
2.  **Analyzes Reports** using a locally-hosted Large Language Model (LLM). An AI "Observer" agent reads unstructured text (like a tweet) and converts it into structured data, identifying the issue type and assessing its priority.
3.  **Dispatches Alerts** for high-priority issues. A "Dispatcher" agent takes the structured data and uses tools to take action, like sending an SMS alert to on-call personnel via the Twilio API.
4.  **Visualizes Issues** on a live, map-based dashboard, giving city managers a real-time overview of the operational status of their city.

## 🎬 Live Demo

*It's highly recommended to record a short GIF of your application in action (e.g., posting a tweet, seeing the marker appear on the map, and showing the SMS alert) and embed it here. A visual demo is incredibly powerful.*



---

## 🏗️ System Architecture

The application is built with a modern, modular architecture to separate concerns and ensure scalability.

1.  **Data Ingestion Layer**:
    * Connects to external services like the Twitter/X API and other city data sources.
    * Responsible for fetching raw, real-time data.

2.  **Backend Core (FastAPI)**:
    * **API Server**: Provides a REST API for the frontend.
    * **Background Worker**: A periodic task that continuously runs the data processing pipeline.
    * **Agentic Core (LangChain + Ollama)**: The "brain" of the operation.
        * `Observer Agent`: Uses a local Llama 3 model to perform NLU, entity extraction, and prioritization.
        * `Dispatcher Agent`: A simple rules-based agent that decides which action to take based on the Observer's analysis.
    * **Action Layer**: A set of "tools" the agents can use, such as the `Twilio Tool` for sending SMS alerts.

3.  **Frontend (React)**:
    * A single-page application built with Vite and React.
    * Continuously polls the backend for new issues.
    * Uses **Leaflet** to render an interactive, real-time map of all detected issues.



---

## 🛠️ Tech Stack

| Category      | Technology / Library                                                                                                |
| :------------ | :------------------------------------------------------------------------------------------------------------------ |
| **Backend** | Python, FastAPI, Uvicorn, Tweepy, Twilio                                                                            |
| **AI / LLM** | LangChain (for agent orchestration), Ollama (for serving the LLM), Llama 3 (8B model)                                 |
| **Frontend** | JavaScript, React, Vite, Axios, Leaflet, React-Leaflet                                                              |
| **DevOps** | Git, GitHub, Virtual Environments (`venv`), `npm`                                                                   |

---

## 🚀 Getting Started / How to Run Locally

Follow these steps to set up and run the project on your local machine.

### Prerequisites

* **Git**: To clone the repository.
* **Python 3.10+**: For the backend.
* **Node.js 18+** and **npm**: For the frontend.
* **Ollama**: To run the local LLM. [Download and install it here](https://ollama.com/).

### 1. Clone the Repository

```bash
git clone [https://github.com/YOUR_USERNAME/civicsense-ai.git](https://github.com/YOUR_USERNAME/civicsense-ai.git)
cd civicsense-ai
```

### 2. Backend Setup

1.  Navigate to the backend directory:
    ```bash
    cd backend
    ```

2.  Create and activate a Python virtual environment:
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  Create a `.env` file for your secrets. Copy the example file:
    ```bash
    cp .env.example .env
    ```
    Now, open the `.env` file and fill in your actual API keys from Twilio and Twitter/X.

4.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

5.  Pull the Llama 3 model using Ollama. (This may take some time and requires ~5GB of disk space).
    ```bash
    ollama pull llama3
    ```

### 3. Frontend Setup

1.  In a **new terminal**, navigate to the frontend directory:
    ```bash
    cd frontend
    ```
2.  Install the required Node.js packages:
    ```bash
    npm install
    ```

### 4. Running the Application

You need to have both the backend and frontend servers running simultaneously.

1.  **Start the Backend Server** (in your first terminal, inside `/backend`):
    ```bash
    uvicorn main:app --reload
    ```
    The backend is now running on `http://127.0.0.1:8000`.

2.  **Start the Frontend Server** (in your second terminal, inside `/frontend`):
    ```bash
    npm run dev
    ```
    The application will automatically open in your browser at `http://localhost:5173`.

You should now see the live dashboard! The backend will start fetching data, and markers will appear on the map as issues are processed.

---

## 📈 Project Status & Future Work

* **Status**: This project is a functional prototype developed in under 4 days for the Hacktivism II hackathon.

* **Future Enhancements**:
    * **Advanced Analyst Agent**: Implement a more sophisticated agent that can detect trends and predict cascading failures (e.g., a power outage causing traffic light failures).
    * **More Data Sources**: Integrate with real-time public transit feeds (GTFS), weather APIs, and IoT sensor data.
    * **Persistent Database**: Replace the in-memory database with a robust solution like PostgreSQL with PostGIS for geospatial queries.
    * **Cloud Deployment**: Containerize the application with Docker and deploy it to a scalable cloud platform like AWS or GCP.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.