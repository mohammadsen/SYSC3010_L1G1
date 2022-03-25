# Unit Test Final Plan 

# ESP32 HardWare
	- Visually Confirm Red Green and blue are shown on the LED STRIP with a 3 Second Delay
	
# ESP32 Software 
	-Run  ESP32TESTS.into

# Alexa Test 
	-Type out 12 Different Intents: 

# SenseHat Software & Harware Test
	-Run Test script [senseHatTempTest.py] which includes two tests
	-First test is the Hardware test which makes sure that the sense Hat is  capable of reading the temperature
	-Second test will test the capability of reading data from the sensehat and then writing it onto firebase and then read that value from firebase and checks if 		it is the same as the original temperature value
	-All test cases should pass

# Raspberry Pi Mic + Speaker 
	-Record and Play audio file

# PIR motion sensor HardWare
	-Run [pirSensor_hardwareTest.py](Test Scripts)
	-Manually make motion in front of the PIR sensor
	-"Motion detected" will be printed on console for verification

# PIR motion sensor Software
	-Run [detectMotion_test.py](Test Scripts)
	-All test cases should pass for verification

# GUI software 
	-Run the [testGUI.py](Test Scripts)
	-The test automatically clicks all the button on the interface and verifies that the right data is pushed into Firebase
