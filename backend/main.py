import asyncio
from fastapi import FastAPI, BackgroundTasks
from typing import List
from fastapi.middleware.cors import CORSMiddleware

# Import our custom modules
from data_ingestion.mock_311_client import fetch_new_reports
from data_ingestion.twitter_client import fetch_new_tweets
from agents.observer import analyze_report
from agents.dispatcher import process_issue

# Initialize FastAPI app
app = FastAPI(title="CivicSense AI Backend")

# Define the list of allowed origins (your frontend's address)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods
    allow_headers=["*"], # Allows all headers
)

# In-memory "database" to store processed issues for the frontend
processed_issues_db: List[dict] = []

async def process_new_data():
    """The core background task that runs the AI pipeline."""
    print("Checking for new data...")

    # 2. CALL THE NEW FUNCTION AND COMBINE DATA
    all_reports = []
    # We'll use a simple try-except block for robustness
    try:
        all_reports.extend(fetch_new_reports())
    except Exception as e:
        print(f"Error fetching 311 reports: {e}")

    try:
        all_reports.extend(fetch_new_tweets())
    except Exception as e:
        print(f"Error fetching tweets: {e}")

    for report in all_reports:
        # Important: We now check for a unique ID to avoid duplicates
        if any(p.get("original_id") == report["id"] for p in processed_issues_db):
            continue

        print(f"New report found (ID: {report['id']}): {report['text']}")
        analysis = analyze_report(report['text'])

        if analysis:
            # Add original ID and text for context and duplicate checking
            analysis["original_id"] = report["id"]
            analysis["original_text"] = report["text"]
            process_issue(analysis)
            processed_issues_db.append(analysis)

async def periodic_task():
    """Runs the data processing task every N seconds."""
    while True:
        await process_new_data()
        await asyncio.sleep(70) # Poll for new data every 70 seconds

@app.on_event("startup")
async def startup_event():
    """Start the background task when the server starts."""
    asyncio.create_task(periodic_task())

@app.get("/")
def read_root():
    return {"status": "CivicSense AI Backend is running."}

@app.get("/api/issues")
def get_issues() -> List[dict]:
    """API endpoint for the frontend to fetch processed issues."""
    return processed_issues_db