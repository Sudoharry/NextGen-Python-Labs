import tkinter as tk
from tkinter import messagebox
import pywhatkit
import smtplib
from twilio.rest import Client
import datetime

# Twilio Configuration (Replace with your real credentials)
TWILIO_SID = 'AC4c2bc2466afef087f51274542a8a2733'
TWILIO_AUTH_TOKEN = '9f092d0602b91badb2b7b43899952973'
TWILIO_PHONE = '+19898228631'  # your Twilio number

# Email Configuration
EMAIL = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_app_password'

def send_whatsapp():
    number = entry_number.get()
    message = entry_message.get("1.0", tk.END).strip()
    now = datetime.datetime.now()
    hour, minute = now.hour, now.minute + 2
    try:
        pywhatkit.sendwhatmsg(number, message, hour, minute, wait_time=10)
        messagebox.showinfo("Success", "WhatsApp message scheduled successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def send_email():
    recipient = entry_email.get()
    subject = "Message from Python GUI"
    message = entry_message.get("1.0", tk.END).strip()
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, EMAIL_PASSWORD)
        email_body = f"Subject: {subject}\n\n{message}"
        server.sendmail(EMAIL, recipient, email_body)
        server.quit()
        messagebox.showinfo("Success", "Email sent!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def send_sms():
    number = entry_number.get()
    message = entry_message.get("1.0", tk.END).strip()
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE,
            to=number
        )
        messagebox.showinfo("Success", "SMS sent!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Message Sender")
root.geometry("400x400")

tk.Label(root, text="Phone Number (+91...)").pack()
entry_number = tk.Entry(root, width=40)
entry_number.pack()

tk.Label(root, text="Email Address").pack()
entry_email = tk.Entry(root, width=40)
entry_email.pack()

tk.Label(root, text="Message").pack()
entry_message = tk.Text(root, height=5, width=40)
entry_message.pack()

tk.Button(root, text="Send WhatsApp", command=send_whatsapp).pack(pady=5)
tk.Button(root, text="Send Email", command=send_email).pack(pady=5)
tk.Button(root, text="Send SMS", command=send_sms).pack(pady=5)

root.mainloop()
