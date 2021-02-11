import os
from twilio.rest import Client
from scrape_two_sms import get_sports_job_postings

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


message = client.messages \
                .create(
                     body=get_sports_job_postings(),
                     from_=os.environ['TWILIO_PHONE'],
                     to=os.environ['MY_PHONE']
                 )

print(message.sid)