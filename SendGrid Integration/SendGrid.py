import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
message = Mail(
from_email="sender@gmail.com", 
to_emails="receiver@gmail.com", 
subject="test",
html_content="<p>welcome to sendgrid with python</hi>"
)
try:
    sg = SendGridAPIClient("XXXX API key XXXXXX") 
    response = sg.send(message)
except Exception as e: 
    print(e)
