from twilio.rest import Client

# Twilio credentials (from your Twilio account)
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
from_number = '+1415XXXXXXX'  # Your Twilio phone number
to_number = '+91XXXXXXXXXX'   # Receiver's phone number

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello! This is a test SMS from Python 🚀",
    from_=from_number,
    to=to_number
)

print("✅ SMS sent:", message.sid)
