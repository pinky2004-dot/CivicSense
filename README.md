# CivicSense

*A stateful, multi-agent AI system for proactive civic issue detection and analysis.*

[![Hacktivism II](https://img.shields.io/badge/Hackathon-Hacktivism%20II-blueviolet)](https://hacktivism-2.devpost.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18-61DAFB?logo=react)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?logo=fastapi)](https://fastapi.tiangolo.com/)

---

## Table of Contents

1.  [Overview](#-overview)
2.  [System Architecture](#-system-architecture)
3.  [Tech Stack](#-tech-stack)
4.  [Getting Started](#-getting-started)
5.  [Running the Application](#-running-the-application)
6.  [API Endpoint](#-api-endpoint)
7.  [Project Roadmap](#-project-roadmap)
8.  [License](#-license)

---

##  Overview

Municipal management of civic issues—potholes, power outages, public hazards—is fundamentally **reactive**. It depends on citizen reports processed through slow, manual triage systems. This latency between an event's occurrence and its resolution can impact public safety and quality of life.

**CivicSense** is an architectural paradigm shift. It operates as a proactive, autonomous system that constantly monitors a city's digital pulse. By employing a collaborative team of specialized AI agents, it not only detects and classifies individual issues in real-time but also analyzes patterns and trends to generate higher-level insights, enabling city officials to address problems before they escalate.

---

##  System Architecture

The system is designed as a **stateful, multi-agent application**. This is a departure from simple stateless scripts, allowing the system to maintain a memory of events and perform complex analysis over time.

```mermaid
graph TD
    subgraph External Sources
        A[Twitter/X API]
        B[Mock 311 Reports]
    end

    subgraph Backend Core (FastAPI)
        C[Polling Task] --> D{Observer Agent};
        D --> E[City State Manager];
        F[Analysis Task] --> G{Analyst Agent};
        G --> E;
        E --> G;
        E --> H{Dispatcher Agent};
        H --> I{Communicator Agent};
        I --> J[Twilio API];
        E --> K[API Endpoint /api/state];
    end
    
    subgraph Frontend (React)
        L[React UI] --> K;
    end
    
    A --> C;
    B --> C;
    K --> L;
```

### Components

* **Data Ingestion**: A background polling task (`Polling Task`) runs continuously to fetch new data from external sources.
* **City State Manager**: A central, in-memory database that holds the current state of all `active_issues` and `generated_insights`. It serves as the single source of truth for the entire system.
* **The Agentic Team**: A collaborative group of four specialized AI agents built with LangChain.
    1.  **`Observer` Agent**: The "eyes and ears." It ingests raw, unstructured text and uses an LLM to parse it into a structured `Issue` object with a type, summary, and priority.
    2.  **`Analyst` Agent**: The "strategic brain." It runs on a separate, less frequent schedule. It reads the entire list of active issues from the `City State` and uses an LLM to perform semantic clustering, identifying patterns and creating high-level `Insight` objects.
    3.  **`Dispatcher` Agent**: The "traffic cop." It receives new `Issues` and `Insights` and determines the appropriate action protocol based on predefined rules (e.g., a high-priority issue requires an immediate SMS).
    4.  **`Communicator` Agent**: The "voice." It receives tasks from the `Dispatcher` and is responsible for all external communication. It formats messages and uses tools like the Twilio API to send alerts.
* **Backend API (FastAPI)**: A robust Python server that orchestrates the background tasks and exposes a single `/api/state` endpoint for the frontend.
* **Frontend UI (React)**: A responsive, map-based dashboard built with Vite and React. It polls the backend for the latest state and visualizes issues and insights in real-time using Leaflet.

---

##  Tech Stack

| Category | Technology / Library | Purpose |
| :--- | :--- | :--- |
| **Backend** | Python 3.11, FastAPI, Uvicorn | Core server, API routing, and asynchronous tasks. |
| | Tweepy, Twilio | Interacting with Twitter/X and Twilio APIs. |
| **AI / LLM** | LangChain, LangChain-Ollama | Orchestrating the agentic workflows. |
| | Ollama, Llama 3 (8B) | Serving the local Large Language Model for AI reasoning. |
| | Pydantic | Data validation and structuring for AI outputs. |
| **Frontend** | JavaScript, React 18, Vite | Modern, fast frontend development and UI. |
| | Axios, Leaflet, React-Leaflet | API communication and interactive map rendering. |
| **DevOps** | Git, GitHub, venv, npm | Version control and dependency management. |

---

##  Getting Started

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
3.  Create a `.env` file for your secrets. A `.env.example` file is provided.
    ```bash
    # Copy the example file
    cp .env.example .env
    ```
    Now, open the newly created `.env` file and fill in your actual API keys from Twilio and Twitter/X.

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

---

##  Running the Application

You must have both the backend and frontend servers running simultaneously.

1.  **Start the Backend Server** (in your first terminal, inside `/backend`):
    ```bash
    uvicorn main:app --reload
    ```
    The backend is now running on `http://127.0.0.1:8000` and will start its background tasks.

2.  **Start the Frontend Server** (in your second terminal, inside `/frontend`):
    ```bash
    npm run dev
    ```
    The application will automatically open in your browser at `http://localhost:5173`.

You should now see the live dashboard! The backend will start fetching data, and markers and insights will appear on the UI as they are processed.

---

##  API Endpoint

The application uses a single endpoint to provide the full state to the frontend.

* **`GET /api/state`**
    * **Description**: Retrieves the current list of active issues and generated insights.
    * **Response Body**:
        ```json
        {
          "active_issues": [
            {
              "issue_type": "string",
              "summary": "string",
              "priority": "string",
              "location": "[lat, lon]",
              "original_id": "number"
            }
          ],
          "generated_insights": [
            {
              "title": "string",
              "summary": "string",
              "priority": "string"
            }
          ]
        }
        ```

---

##  Project Roadmap

This project serves as a robust prototype with a clear path for future enhancements:

* **Persistent Database**: Replace the in-memory `CityState` manager with a robust database like PostgreSQL with the PostGIS extension for efficient geospatial querying.
* **Expanded Data Sources**: Integrate with more real-time data streams, such as public transit feeds (GTFS-RT), weather APIs, and municipal IoT sensors.
* **Advanced `Analyst` Capabilities**: Enhance the `Analyst` agent to perform predictive analytics (e.g., predicting infrastructure failures based on age and weather patterns).
* **Containerization & Deployment**: Containerize the application with Docker and deploy it to a scalable cloud platform like AWS or GCP for production use.

---

##  License

This project is licensed under the MIT License. See the `LICENSE` file for details.