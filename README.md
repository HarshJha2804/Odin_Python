# OTP Verification System

## Introduction
This project is a simple OTP (One-Time Password) verification system built with Python and Tkinter. It generates a 6-digit OTP, sends it via email using Gmail's SMTP server, and allows the user to verify the OTP through a graphical interface.

## Features
- Generates a **6-digit OTP**
- Sends OTP via **email**
- Provides a **GUI interface** for user interaction
- Verifies OTP entered by the user
- Displays error messages for incorrect OTP or authentication failures

## Requirements
- Python 3.x
- Gmail account with **App Password** enabled
- Required Python libraries:
  ```bash
  pip install tkinter
  ```

## Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/otp-verification.git
cd otp-verification
```

### 2. Configure Environment Variables
Set up your email credentials as environment variables:
```bash
export SENDER_EMAIL="your-email@gmail.com"
export SENDER_PASSWORD="your-app-password"
```

### 3. Run the Application
```bash
python otp_verification.py
```

### 4. Usage Steps
1. Click **"Send OTP"** – OTP is generated and sent to the registered email.
2. Enter the **OTP** received in the email.
3. Click **"Verify OTP"** – If correct, access is granted; otherwise, an error message is shown.

## Error Handling
- **Incorrect OTP:** Displays an error message.
- **Invalid Credentials:** Prompts authentication failure.
- **SMTP Connection Issues:** Shows relevant error messages.

## Future Enhancements
- Store OTPs in a database
- Implement OTP expiration handling
- Support for **SMS-based OTP** verification using Twilio

## License
This project is open-source and available under the **MIT License**.

## Author
Developed by **[Harsh Jha]**

---
Feel free to contribute and improve this project! 🚀

