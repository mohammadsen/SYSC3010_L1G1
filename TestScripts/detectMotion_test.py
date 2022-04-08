import unittest
import pyrebase
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

class TestMotion(unittest.TestCase):

    def test_motion_off(self):
        # Each 'child' is a JSON key:value pair 
        db.child(dataset).child("Motion detected").set(0)
        time.sleep(3)
        motion = db.child(dataset).get()
        motion_list = motion.each() 
        lastDataPoint = motion_list[-1]
        
        self.assertEqual(lastDataPoint.val(), 0, "Should be 0")
        
    def test_motion_on(self):
        # Each 'child' is a JSON key:value pair 
        db.child(dataset).child("Motion detected").set(1)
        time.sleep(3)
        motion = db.child(dataset).get()
        motion_list = motion.each() 
        lastDataPoint = motion_list[-1]
        
        self.assertEqual(lastDataPoint.val(), 1, "Should be 1")
        
    def test_motion_on_1(self):
        # Each 'child' is a JSON key:value pair 
        db.child(dataset).child("Motion detected").set(1)
        time.sleep(3)
        motion = db.child(dataset).get()
        motion_list = motion.each() 
        lastDataPoint = motion_list[-1]
        
        self.assertFalse(lastDataPoint.val()==0, "Should be 1")
        
    def test_motion_off_1(self):
        # Each 'child' is a JSON key:value pair 
        db.child(dataset).child("Motion detected").set(0)
        time.sleep(3)
        motion = db.child(dataset).get()
        motion_list = motion.each() 
        lastDataPoint = motion_list[-1]
        
        self.assertFalse(lastDataPoint.val()==1, "Should be 0")
        

if __name__ == '__main__':
    unittest.main()