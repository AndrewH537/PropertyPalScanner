import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(new_listings):
    logging.info("Preparing to send email.")
    
    sender_email = 'yourEmail@test.com'
    receiver_email = 'yourEmail@test.com'
    password = 'yourEmailPassword'
    
    subject = 'New Property Listings'
    body = '\n\n'.join([f"Address: {listing['address']}\nPrice: {listing['price']}\nLink: {listing['link']}" for listing in new_listings])
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        logging.info("Email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
