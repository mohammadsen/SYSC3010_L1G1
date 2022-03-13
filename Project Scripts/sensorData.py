#from pyrebase import pyrebase
import pyrebase
import random 
import time
from sense_hat import SenseHat
#sensorData = SenseHat()
from time import sleep
 
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
    while True: 
        # I'm using dummy sensor data here, you could use your senseHAT
        sensorData = SenseHat()
        temperature = sensorData.get_temperature()
        db.child(dataset).child("Temperature").set(temperature) 
        time.sleep(3) 
   
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


