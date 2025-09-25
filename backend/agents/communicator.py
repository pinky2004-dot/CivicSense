from tools.twilio_tool import send_sms_alert

def handle_communication(task: str, details: dict):
    """
    Handles crafting and sending communications based on a task.
    """
    print(f"Communicator received task: {task}")
    
    if task == "SEND_HIGH_PRIORITY_SMS":
        # Here, use an LLM to generate a more detailed message if needed.
        # For now, I'll pass the details directly to the Twilio tool.
        send_sms_alert(details)
    elif task == "DRAFT_WEEKLY_SUMMARY":
        print("Communicator is drafting a weekly summary (not implemented).")
    else:
        print(f"Communicator does not know how to handle task: {task}")