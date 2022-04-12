import pyrebase
from sense_hat import SenseHat
from twilio.rest import Client
import math
import sqlite3
import time
from datetime import datetime

dbconnect = sqlite3.connect("my.db")
dbconnect.row_factory = sqlite3.Row
cursor = dbconnect.cursor()

# Create new Firebase config and database object
config = {
    "apiKey": "AIzaSyCjM2ldLom7MMcyHelKZoOxyMz0sJBbLeQ",
    "authDomain": "l1g1finalfirebase.firebaseapp.com",
    "databaseURL": "https://l1g1finalfirebase-default-rtdb.firebaseio.com/",
    "storageBucket": "l1g1finalfirebase.appspot.com",
}

TWILIO_ACCOUNT_SID = "ACdd449690e811a96db39f25303eea3bfe"  # Twilio Account SID
TWILIO_AUTH_TOKEN = "5d18f7d9aa23cfe7e1cd3c9247c86abd"  # Twilio Account Auth Token
TWILIO_PHONE_SENDER = "+17579066754"  # Phone number registered in twilio
TWILIO_PHONE_RECIPIENT = "+13437776499"  # Phone number message will be sent to

firebase = pyrebase.initialize_app(config)
db = firebase.database()
dataset0 = "sensorData"
dataset1 = "Motion"
dataset2 = "LedStatus"


def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS local(Temperature NUMERIC, MotionDetected INTEGER, LEDeffect INTEGER, LEDstatus INTEGER)')
    cursor.execute('CREATE TABLE IF NOT EXISTS motion0(MotionDetected INTEGER, Date DATETIME)')

# Sens an sms Text to the designated phone number
def send_text_alert(alert_str):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(to=TWILIO_PHONE_RECIPIENT, from_=TWILIO_PHONE_SENDER, body=alert_str)


def readData():
    
    while True:
        
        
        # writing into firebase
        sensorData = SenseHat()
        temp = sensorData.get_temperature()
        temperature = math.floor(temp)
        db.child(dataset0).child("Temperature").set(temperature)
        print(temperature)
        
        # Reading from FireBase
        mySensorData = db.child(dataset0).get()
        # Returns the dictionary as a list
        mySensorData_list = mySensorData.each() 
        # Takes the last element of the list 
        lastDataPoint = mySensorData_list[-1] 
        print("SensorData: {}\n".format(lastDataPoint.val()))
    
        myMotionData = db.child(dataset1).get()
        myMotionData_list = myMotionData.each()
        lastDataPoint1 = myMotionData_list[-1]
        print("MotionData: {}\n".format(lastDataPoint1.val()))
    
        myLedEffectData = db.child(dataset2).get(0)
        myLedEffectData_list = myLedEffectData.each()
        lastDataPoint2 = myLedEffectData_list[0]
        print("LedEffectData: {}\n".format(lastDataPoint2.val()))
    
        myLedStatusData = db.child(dataset2).get()
        myLedStatusData_list = myLedStatusData.each()
        lastDataPoint3 = myLedStatusData_list[-1]
        print("LedStatusData: {}\n".format(lastDataPoint3.val()))
        lightStatus = lastDataPoint3.val(); 
        date = datetime.now()
        cursor.execute('''insert into local values(?, ?, ?, ?)''', (lastDataPoint.val(), lastDataPoint1.val(), lastDataPoint2.val(), lastDataPoint3.val()));
        #cursor.execute('''insert into motion0 values(?, ?)''', (lastDataPoint1.val(), date));
        dbconnect.commit();
        cursor.execute('SELECT * FROM local');
        #cursor.execute('SELECT * FROM motion0');
        time.sleep(10)
        #dbconnect.close();
        
        sentMessage =0;
        if (lightStatus==1 and sentMessage == 0):
            send_text_alert('The light has been turned on');
            sentMessage =1;
            

#def main:
create_table()
readData()


#if __name__ == '__main__':
#    main()
