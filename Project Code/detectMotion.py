import pyrebase
import random 
import RPi.GPIO as GPIO
import time
import datetime

# Create new Firebase config and database object 
config = {
          "apiKey": "AIzaSyCjM2ldLom7MMcyHelKZoOxyMz0sJBbLeQ",
          "authDomain": "l1g1finalfirebase.firebaseapp.com",
          "databaseURL": "https://l1g1finalfirebase-default-rtdb.firebaseio.com/",
          "storageBucket": "l1g1finalfirebase.appspot.com",
}
 
firebase = pyrebase.initialize_app(config) 
db = firebase.database() 
dataset = "Motion"

PIR    = 23
GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)

#Next iteration we are going to implement the mMotion sensor in a way that
#if a person walks by it turns on and when th person walks by a second time,
#it turns off.

def writeData():
    try:

        while True:
            time.sleep(1)
            motionDetected=0
            if GPIO.input(PIR) == 1:
                print("Is motion detected?")
                motionDetected=1
            
            else:
                print("Is motion detected?")
            
            print(motionDetected)
            
            # Each 'child' is a JSON key:value pair 
            db.child(dataset).child("Motion detected").set(motionDetected)
            time.sleep(3)
              
    except KeyboardInterrupt:
        GPIO.cleanup()
        
def readData():
    # Create new Firebase config and database object 
    config = { 
              "apiKey": "AIzaSyCjM2ldLom7MMcyHelKZoOxyMz0sJBbLeQ",
              "authDomain": "l1g1finalfirebase.firebaseapp.com",
              "databaseURL": "https://l1g1finalfirebase-default-rtdb.firebaseio.com/",
              "storageBucket": "l1g1finalfirebase.appspot.com",
    } 
 
    firebase = pyrebase.initialize_app(config) 
    db = firebase.database() 
    dataset = "Motion"
  
    # Returns the entry as an ordered dictionary (parsed from json) 
    mySensorData = db.child(dataset).get()
    print(mySensorData.val())
 
    print("Parent Key: {}".format(mySensorData.key())) 
    print("Parent Value: {}\n".format(mySensorData.val())) 
 
    # Returns the dictionary as a list
    mySensorData_list = mySensorData.each() 
    # Takes the last element of the list 
    lastDataPoint = mySensorData_list[-1] 
 
    print("Child Key: {}".format(lastDataPoint.key())) 
    print("Child Value: {}\n".format(lastDataPoint.val()))  

def main():
    writeData()
    readData()
if __name__ == "__main__": 
    main()
