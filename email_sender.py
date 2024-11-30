import smtplib
import getpass
import sys

try:
    # Connecting to Gmail server
    smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
    
    # Server greeting and start TLS
    print(smtp_obj.ehlo())
    print(smtp_obj.starttls())

    # Get email credentials securely
    email = getpass.getpass("Enter sender email: ")
    password = getpass.getpass("Enter sender app password please: ")

    try:
        # Login to the server
        print(smtp_obj.login(email, password))

        # Get recipient and message details
        to_address = getpass.getpass("Enter receiver mail: ")
        subject = input("Enter the subject of mail: ")
        body = input("Enter the body of mail: ")

        # Construct the message
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        smtp_obj.sendmail(email, to_address, message)
        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email and app password.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")

except Exception as e:
    print(f"Connection error: {e}")
finally:
    # Ensure the SMTP connection is closed
    if 'smtp_obj' in locals():
        smtp_obj.quit()