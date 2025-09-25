from typing import List, Dict, Any

class CityState:
    """A simple in-memory database to hold the application's state."""
    def __init__(self):
        self.active_issues: List[Dict[str, Any]] = []
        self.generated_insights: List[Dict[str, Any]] = []

    def add_issue(self, issue: Dict[str, Any]):
        # Avoid adding duplicate issues
        if not any(p.get("original_id") == issue["original_id"] for p in self.active_issues):
            self.active_issues.append(issue)
            print(f"State: New issue added (ID: {issue['original_id']}). Total issues: {len(self.active_issues)}")

    def add_insight(self, insight: Dict[str, Any]):
        self.generated_insights.append(insight)
        print(f"State: New insight generated. Total insights: {len(self.generated_insights)}")

# Create a single, shared instance of state
city_state = CityState()