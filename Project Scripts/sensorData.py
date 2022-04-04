#from pyrebase import pyrebase
import pyrebase
import random 
import time
from sense_hat import SenseHat
#sensorData = SenseHat()
from time import sleep
import sendsms
import math
# Create new Firebase config and database object 
config = {
          "apiKey": "AIzaSyCjM2ldLom7MMcyHelKZoOxyMz0sJBbLeQ",
          "authDomain": "l1g1finalfirebase.firebaseapp.com",
          "databaseURL": "https://l1g1finalfirebase-default-rtdb.firebaseio.com/",
          "storageBucket": "l1g1finalfirebase.appspot.com",
} 

firebase = pyrebase.initialize_app(config)
db = firebase.database()
dataset = "sensorData"

# Write random numbers to database
def writeData(): 
        # writing into firebase
        sensorData = SenseHat()
        temp = sensorData.get_temperature()
        temperature = math.floor(temp)
        db.child(dataset).child("Temperature").set(temperature)
        sendsms.send_text_alert(temperature)

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
    dataset = "sensorData"

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
