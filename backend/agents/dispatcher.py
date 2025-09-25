def process_event(event_type: str, data: dict) -> str | None:
    """
    Processes an event (a new issue or insight) and returns a communication task if needed.
    """
    print(f"Dispatcher received event: {event_type} with data: {data}")
    
    priority = data.get("priority", "Low")
    
    if event_type == "NEW_ISSUE" and priority == "High":
        return "SEND_HIGH_PRIORITY_SMS"
        
    if event_type == "NEW_INSIGHT":
        # For now, I don't have an action for insights, but I could add one here.
        # For example: return "DRAFT_WEEKLY_SUMMARY"
        pass
        
    return None # No action needed