from twilio.rest import Client

TWILIO_ACCOUNT_SID = 'ACdd449690e811a96db39f25303eea3bfe' # replace with your Account SID
TWILIO_AUTH_TOKEN = '5d18f7d9aa23cfe7e1cd3c9247c86abd' # replace with your Auth Token
TWILIO_PHONE_SENDER = "+17579066754" # replace with the phone number you registered in twilio
TWILIO_PHONE_RECIPIENT = "+13437776499" # replace with your phone number

def send_text_alert(alert_str):
    """Sends an SMS text alert."""
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=TWILIO_PHONE_RECIPIENT,
        from_=TWILIO_PHONE_SENDER,
        body=alert_str)
    print(message.sid)
    
#def main():
    
#     send_text_alert("Isha3la2")
 
#if __name__ == "__main__": 
#    main()