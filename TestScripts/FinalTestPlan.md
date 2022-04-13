# Unit Test Final Plan 

# ESP32 HardWare
	- Visually Confirm Red Green and blue are shown on the LED STRIP with a 3 Second Delay
	
# ESP32 Software 
	- To test the Sofware portion of the ESP32, You must run and Upload the L1G1ESP32_TestCases.ino file onto your ESP32. You must then open the Serial Monitor (CMD + Shift + M)
	- As the ESP32 runs through the Code, you should monitor the serial monitor. There will be 4 test cases which should pass as indicated in the serial moniotor 

# Alexa Test 
	-Type out or speak the following 13 Different Intents: 
		- "Alexa Open Light Control"
		- "Alexa tell Light Control to turn lights on"
		- "Alexa tell Light Control to turn lights off"
		- "Alexa tell Light Control to get temperature"
		- "Alexa tell Light Control to Change Light strip to *color*" -> One of the Colors found in the GUI
	- The expected result is that the Light strips should change as commanded except for when Alexa is asked about the Temperature. Alexa should Reply with the temperature value in Degrees Celcius .
	


# SenseHat Software & Harware Test
	-Run Test script [senseHatTempTest.py] which includes two tests
	-First test is the Hardware test which makes sure that the sense Hat is  capable of reading the temperature
	-Second test will test the capability of reading data from the sensehat and then writing it onto firebase and then read that value from firebase and checks 	     if it is the same as the original temperature value
	-All test cases should pass

# Push Notifications 
	-Run [sensorData.py] and [detectMotion.py]
	-After running [sensorData.py] which writes the temperature value onto firebase, a notification will be sent as an sms with the temperature value
	-After running [detectMotion.py] which chcecks if there's motion detected, a notification will be sent as an sms with the message "motionDetected" 

# Raspberry Pi Mic + Speaker 
	-Copy and Paste commands From RaspiHarware.txt
	- The audio file that is created should be a recording of your voice 

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
