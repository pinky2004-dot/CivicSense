import random

# In a real app, this would make an API call. For the hackathon, we simulate it.
MOCK_REPORTS = [
    {"id": 1, "text": "Huge pothole on the corner of Preston Rd and Glendenning Ln. Cars are swerving to avoid it."},
    {"id": 2, "text": "The traffic lights at the main intersection of Frontier Pkwy are completely out. It's a major safety hazard."},
    {"id": 3, "text": "Graffiti on the park bench near the splash pad."},
    {"id": 4, "text": "Power lines are down behind city hall after that storm, sparks are flying."},
]

def fetch_new_reports():
    """Simulates fetching a new report from a 311 system."""
    # Return one random report to simulate a new event.
    return [random.choice(MOCK_REPORTS)]