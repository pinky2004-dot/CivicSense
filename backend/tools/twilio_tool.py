from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, YOUR_CELL_PHONE_NUMBER

def send_sms_alert(issue_details: dict):
    """Sends an SMS alert using Twilio."""
    if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, YOUR_CELL_PHONE_NUMBER]):
        print("Twilio credentials not fully configured. Skipping SMS.")
        return

    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message_body = (
            f"🚨 HIGH PRIORITY ALERT 🚨\n\n"
            f"Issue: {issue_details.get('issue_type', 'N/A')}\n"
            f"Summary: {issue_details.get('summary', 'N/A')}"
        )

        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=YOUR_CELL_PHONE_NUMBER
        )
        print(f"SMS alert sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS: {e}")