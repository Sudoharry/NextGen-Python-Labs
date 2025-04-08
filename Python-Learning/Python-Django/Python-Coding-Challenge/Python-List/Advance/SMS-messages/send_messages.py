import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "harendrabarot19@gmail.com"
receiver_email = "harendrabarot19@example.com"
password = "Hb_8849964295"  # Enable 2FA and generate App Password

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Hello from Python!"

body = "This is a test email sent via Python!"
message.attach(MIMEText(body, "plain"))

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("✅ Email sent successfully.")
