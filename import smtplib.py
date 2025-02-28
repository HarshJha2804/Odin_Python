import smtplib
import random
import os
import tkinter as tk
from tkinter import messagebox
from email.mime.text import MIMEText

# Get credentials from environment variables
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "jha.harsh17@gmail.com")  # Use your Gmail
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD", "nkmxpupgfjlvhmpu")  # App Password (No spaces)
RECIPIENT_EMAIL = "jha.harsh17@gmail.com"  # Replace with recipient email

# OTP expiration time (minutes)
OTP_EXPIRATION = 5
generated_otp = None  # To store the generated OTP


def generate_otp():
    """Generate a 6-digit OTP."""
    return str(random.randint(100000, 999999))


def send_otp_email():
    """Send OTP via Gmail SMTP and update the label."""
    global generated_otp
    generated_otp = generate_otp()
    
    subject = "Your OTP Code"
    body = f"Your OTP code is: {generated_otp}. It expires in {OTP_EXPIRATION} minutes."

    msg = MIMEText(body)
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = subject

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())

        messagebox.showinfo("Success", f"OTP sent successfully to {RECIPIENT_EMAIL}!")
    
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Error", "Authentication failed. Check your App Password.")
    
    except Exception as e:
        messagebox.showerror("Error", f"Error sending OTP: {e}")


def verify_otp():
    """Verify if the entered OTP matches the generated OTP."""
    user_otp = otp_entry.get().strip()

    if user_otp == generated_otp:
        messagebox.showinfo("Success", "OTP verified successfully! Access granted.")
        root.destroy()  # Close the GUI after successful verification
    else:
        messagebox.showerror("Error", "Invalid OTP. Please try again.")


# Create GUI
root = tk.Tk()
root.title("OTP Verification System")
root.geometry("400x300")
root.configure(bg="#f4f4f4")

# Title Label
tk.Label(root, text="OTP Verification", font=("Arial", 16, "bold"), bg="#f4f4f4").pack(pady=10)

# Send OTP Button
send_button = tk.Button(root, text="Send OTP", font=("Arial", 12), command=send_otp_email, bg="#3498db", fg="white")
send_button.pack(pady=10)

# OTP Entry Label
tk.Label(root, text="Enter OTP:", font=("Arial", 12), bg="#f4f4f4").pack()

# OTP Entry Box
otp_entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
otp_entry.pack(pady=5)

# Verify Button
verify_button = tk.Button(root, text="Verify OTP", font=("Arial", 12), command=verify_otp, bg="#2ecc71", fg="white")
verify_button.pack(pady=10)

# Run the GUI
root.mainloop()
