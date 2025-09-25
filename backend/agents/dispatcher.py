from tools.twilio_tool import send_sms_alert

def process_issue(analysis: dict):
    """
    Processes the structured analysis from the Observer
    and decides on the appropriate action.
    """
    if not analysis:
        print("Dispatcher received no analysis to process.")
        return

    print(f"Dispatcher processing issue: {analysis}")
    priority = analysis.get("priority", "Low")

    if priority == "High":
        print("High priority issue detected. Dispatching SMS alert.")
        send_sms_alert(analysis)
    else:
        print(f"'{priority}' priority issue logged. No alert dispatched.")