import unittest
import pyrebase
import time
import datetime
import math
from sense_hat import SenseHat

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

class TestSensorData(unittest.TestCase):

#     Checks if the sensehat was able to read the temperature
    def test_tempGet(unitterst.TestCase):
        sensorData = SenseHat()
        sensorTemperature = sensorData.get_temperature()
        print("sensorTemperature:", sensorTemperature)
        self.assertTrue(sensorTemperature)

#     Checks if the value of the temperature was sent to the firebase and compares it to the value received from the sensehat 
    def test_sensor(self):
        
        # Reading sensorData temperature from the sensor 39.1242790222168 != 38.832794189453125
        sensorData = SenseHat()
        sensorTemperature = sensorData.get_temperature()
        print("sensorTemperature:", sensorTemperature)
        # Reading sensorData temperature from the DB
        dbTemperature = db.child(dataset).child("Temperature").get()
        print("dbTemperature:", dbTemperature.val())
        time.sleep(3)      

        self.assertEqual(math.floor(sensorTemperature), math.floor(dbTemperature.val()))
        

if __name__ == '__main__':
    unittest.main()