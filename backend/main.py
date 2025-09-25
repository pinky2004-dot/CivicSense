import asyncio
from fastapi import FastAPI
import random
from fastapi.middleware.cors import CORSMiddleware

# Import new modules and state
from state import city_state
from data_ingestion.mock_311_client import fetch_new_reports
from data_ingestion.twitter_client import fetch_new_tweets
from agents.observer import analyze_report
from agents.analyst import find_insights
from agents.dispatcher import process_event  # We will create this next
from agents.communicator import handle_communication

app = FastAPI(title="CivicSense AI Backend")
origins = ["http://localhost:5173", "http://127.0.0.1:5173"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# I'll move the dispatcher logic here to act as a central hub
def dispatch(event_type: str, data: dict):
    """Central dispatch function to route events."""
    task = process_event(event_type, data)
    if task:
        handle_communication(task, data)

# --- Background Tasks ---
async def poll_for_new_data():
    """Task 1: Runs frequently to fetch new reports."""
    while True:
        print("Polling for new reports...")
        all_reports = fetch_new_reports() + fetch_new_tweets()
        
        for report in all_reports:
            # Check if issue already exists before expensive LLM call
            if any(p.get("original_id") == report["id"] for p in city_state.active_issues):
                continue

            print(f"New report found (ID: {report['id']}). Sending to Observer.")
            analysis = analyze_report(report['text'])
            if analysis:
                base_location = [33.3240, -96.7828]
                analysis["location"] = [
                    base_location[0] + (random.random() - 0.5) * 0.1,
                    base_location[1] + (random.random() - 0.5) * 0.1,
                ]
                analysis["original_id"] = report["id"]
                city_state.add_issue(analysis)
                dispatch("NEW_ISSUE", analysis) # Dispatch the new issue immediately
        
        await asyncio.sleep(70)

async def run_analysis():
    """Task 2: Runs less frequently to find insights."""
    while True:
        print("Running analysis on active issues...")
        new_insights = find_insights(city_state.active_issues)
        
        for insight in new_insights:
            # Avoid adding duplicate insights
            if not any(i.get("title") == insight["title"] for i in city_state.generated_insights):
                city_state.add_insight(insight)
                dispatch("NEW_INSIGHT", insight) # Dispatch the new insight
        
        await asyncio.sleep(300) # Run analysis every 5 minutes

@app.on_event("startup")
async def startup_event():
    """Starts the background tasks when the server starts."""
    asyncio.create_task(poll_for_new_data())
    asyncio.create_task(run_analysis())

@app.get("/")
def read_root():
    return {"status": "CivicSense AI Agentic System is running."}

@app.get("/api/state")
def get_state():
    """API endpoint for the frontend to fetch the entire city state."""
    return {
        "active_issues": city_state.active_issues,
        "generated_insights": city_state.generated_insights
    }