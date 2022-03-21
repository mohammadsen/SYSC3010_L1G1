import pyrebase
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create new Firebase config and database object 
config = {
          "apiKey": "AIzaSyCjM2ldLom7MMcyHelKZoOxyMz0sJBbLeQ",
          "authDomain": "l1g1finalfirebase.firebaseapp.com",
          "databaseURL": "https://l1g1finalfirebase-default-rtdb.firebaseio.com/",
          "storageBucket": "l1g1finalfirebase.appspot.com",
}
 
firebase = pyrebase.initialize_app(config) 
db = firebase.database() 
dataset = "LedStatus"

 
driver=webdriver.Chrome()
driver.get("file:///home/pi/SYSC3010_L1G1/GUI/index.html")
print(driver.title)

# Testing the "Turn off" button : Test1
driver.find_element(By.ID,"button2").click()
# Returns the entry as an ordered dictionary (parsed from json) 
users = db.child(dataset).get() 
# Returns the dictionary as a list
users_list = users.each() 
# Takes the LedStatus data
ledStatus = users_list[-1]
# Takes the LedEffect data
ledEffect = users_list[-2]
if ledStatus.val()==0 and ledEffect.val()==0:
    print("Test1 passed")
else:
    print("Test1 failed")
    
time.sleep(1)

# Testing the "Turn on" button : Test2
driver.find_element(By.ID,"button1").click()
# Returns the entry as an ordered dictionary (parsed from json) 
users = db.child(dataset).get() 
# Returns the dictionary as a list
users_list = users.each() 
# Takes the LedStatus data
ledStatus = users_list[-1]
# Takes the LedEffect data
ledEffect = users_list[-2]
if ledStatus.val()==1 and ledEffect.val()==1:
    print("Test2 passed")
else:
    print("Test2 failed")
    
time.sleep(1)

# Testing the "Red" button : Test3
driver.find_element(By.ID,"button3").click()
# Returns the entry as an ordered dictionary (parsed from json) 
users = db.child(dataset).get() 
# Returns the dictionary as a list
users_list = users.each() 
# Takes the LedStatus data
ledStatus = users_list[-1]
# Takes the LedEffect data
ledEffect = users_list[-2]
if ledStatus.val()==1 and ledEffect.val()==2:
    print("Test3 passed")
else:
    print("Test3 failed")
    
time.sleep(1)

# Testing the "Green" button : Test4
driver.find_element(By.ID,"button4").click()
# Returns the entry as an ordered dictionary (parsed from json) 
users = db.child(dataset).get() 
# Returns the dictionary as a list
users_list = users.each() 
# Takes the LedStatus data
ledStatus = users_list[-1]
# Takes the LedEffect data
ledEffect = users_list[-2]
if ledStatus.val()==1 and ledEffect.val()==3:
    print("Test4 passed")
else:
    print("Test4 failed")
    
time.sleep(1)

# Testing the "Blue" button : Test5
driver.find_element(By.ID,"button5").click()
# Returns the entry as an ordered dictionary (parsed from json) 
users = db.child(dataset).get() 
# Returns the dictionary as a list
users_list = users.each() 
# Takes the LedStatus data
ledStatus = users_list[-1]
# Takes the LedEffect data
ledEffect = users_list[-2]
if ledStatus.val()==1 and ledEffect.val()==4:
    print("Test5 passed")
else:
    print("Test5 failed")
    
time.sleep(1)

# Testing the "Yellow" button : Test6
driver.find_element(By.ID,"button6").click()
# Returns the entry as an ordered dictionary (parsed from json) 
users = db.child(dataset).get() 
# Returns the dictionary as a list
users_list = users.each() 
# Takes the LedStatus data
ledStatus = users_list[-1]
# Takes the LedEffect data
ledEffect = users_list[-2]
if ledStatus.val()==1 and ledEffect.val()==5:
    print("Test6 passed")
else:
    print("Test6 failed")
    
time.sleep(1)

# Testing the "Orange" button : Test7
driver.find_element(By.ID,"button7").click()
# Returns the entry as an ordered dictionary (parsed from json) 
users = db.child(dataset).get() 
# Returns the dictionary as a list
users_list = users.each() 
# Takes the LedStatus data
ledStatus = users_list[-1]
# Takes the LedEffect data
ledEffect = users_list[-2]
if ledStatus.val()==1 and ledEffect.val()==6:
    print("Test7 passed")
else:
    print("Test7 failed")
    
time.sleep(1)

# Testing the "Indigo" button : Test8
driver.find_element(By.ID,"button8").click()
# Returns the entry as an ordered dictionary (parsed from json) 
users = db.child(dataset).get() 
# Returns the dictionary as a list
users_list = users.each() 
# Takes the LedStatus data
ledStatus = users_list[-1]
# Takes the LedEffect data
ledEffect = users_list[-2]
if ledStatus.val()==1 and ledEffect.val()==7:
    print("Test8 passed")
else:
    print("Test8 failed")
    
time.sleep(1)

# Testing the "Rose" button : Test9
driver.find_element(By.ID,"button9").click()
# Returns the entry as an ordered dictionary (parsed from json) 
users = db.child(dataset).get() 
# Returns the dictionary as a list
users_list = users.each() 
# Takes the LedStatus data
ledStatus = users_list[-1]
# Takes the LedEffect data
ledEffect = users_list[-2]
if ledStatus.val()==1 and ledEffect.val()==8:
    print("Test9 passed")
else:
    print("Test9 failed")
    
time.sleep(1)

# Testing the "White" button : Test10
driver.find_element(By.ID,"button10").click()
# Returns the entry as an ordered dictionary (parsed from json) 
users = db.child(dataset).get() 
# Returns the dictionary as a list
users_list = users.each() 
# Takes the LedStatus data
ledStatus = users_list[-1]
# Takes the LedEffect data
ledEffect = users_list[-2]
if ledStatus.val()==1 and ledEffect.val()==1:
    print("Test10 passed")
else:
    print("Test10 failed")
    
time.sleep(1)

# Testing the "Cyan" button : Test11
driver.find_element(By.ID,"button11").click()
# Returns the entry as an ordered dictionary (parsed from json) 
users = db.child(dataset).get() 
# Returns the dictionary as a list
users_list = users.each() 
# Takes the LedStatus data
ledStatus = users_list[-1]
# Takes the LedEffect data
ledEffect = users_list[-2]
if ledStatus.val()==1 and ledEffect.val()==9:
    print("Test11 passed")
else:
    print("Test11 failed")
    
time.sleep(1)

# Testing the "StatusIndicator" test box : Test12
driver.find_element(By.ID,"StatusIndicator").click()

driver.quit()