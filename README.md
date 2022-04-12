# SYSC3010_L1G1

## HOME AUTOMATION USING VOICE RECOGNITION SOFTWARE

### TEAM MEMBERS
- Wilson Amoussougbo
- Mohammad Gaffori
- Asser Ibrahim

TA: Zein El-Hajj

## WHAT DOES IT DO?
The objective of this project is to further improve the abilities of Smart Assistant devices by adding a ```PIR sensor``` to detect motion and a ```SenseHat``` to provide the indoor temperature of the user location. Furthermore, we intend to implement the ability to control and change the effects on external ```LED strips``` by using an``` Arduino (ESP32) Microcontroller``` working in conjunction with the smart device. Three Raspberry Pis will be using, each with a different functionality going from the motion detector to the temperature sensor. In fact, whenever motion is detected, the LED strip turns on and the user can also make changes to the light colour using a GUI interface. By doing so, the user experience will increase, and this will ultimately result in an increase of convenience for the user. All the nodes in the project will be communication through a ```Firebase``` database and a ```local SQL``` database will be used to send notification to the user whenever change occurs in the system. Last but not least, Amazon ```Alexa``` will be implemented to make LED effects and get the indoor temperature from the virtual assistant.

## GETTING STARTED WITH THE PROJECT

### HARDWARE
1- Raspberry Pi

2- SenseHat

3- PIR Sensor

4- ESP32 Microcrontroller

5- Microphone and Speaker

6- Breadboard and Jumper wires

### CONFIGURATION
All of the hardware configurations for both the PIR sensor [pir_sensorconfig](Images) and the ESP32 [esp32config](Images) are shown in the [Images](Images) folder.

### INSTALL
In order to get the project running, a few pacakges are needed. You can manually install them  using the command below:
```
sudo apt-get install sense-hat
```
```
pip install pyrebase
```
```
sudo pip3 install twilio
```
```
pip install selenium
```

## SCRIPTS

### [detectMotion](ProjectScripts)
This script is used to detect motion and update Firebase as well as sending text notification to the user.
### [sensorData](ProjectScripts)
This script is used to determine indoor temperature of user location and updated Firebase.
### [ESP32Code](ESP32Code)
This script is used to constantly check Firebase and make the LED strip effects.
### [AlexaSkill](AlexaSkill)
This folder contains all the customized skills used for Amazon Alexa.
### [GUI](GUI)
This folder contains all the ```JavaScript``` and ```HTLM``` code for the GUI interface.

### For testing code/scripts refer to [TestScripts](TestScripts)


## GUIDE
In order to lauch the project properly, all of the hardware have to be set up on 3 different devices ```(Raspberry/ESP32)```. Next would be to run [detectMotion](ProjectScripts) , [sensorData](ProjectScripts) and [ESP32Code](ESP32Code) at the same time. It is important to also have the [GUI](GUI) interface openned. 
```
1- If motion is made in front of the PIR sensor, the LED light should turn on and a notification will be sent to user.
2- If user makes change to GUI, appropriate color effect should be perceived happenning in real time on the LED strip.
3- When user asks for indoor temparature, Alexa should be able to accuratelly answer back.
```

## Set Up 

- To Set Up The ESP32, you just plug it into a wall or a USB Port
- To Set Up The Alexa skill, you must first follow the [following guide] (https://developer.amazon.com/en-US/docs/alexa/custom-skills/steps-to-build-a-custom-skill.html)to create a Custom Hello World Skill: 
- 
open the Alexa App on your phone, or Say Hey Alexa to your Amazon Echo 
- To Set Up The GUI, you type into the terminal:
```
$ ngrok http 8080
```
and use one of the Redirection Links

- To Set Up the local database  & SMS push notifications, you run LocalDB.py
- To Set up the motion detection, you aim the Motion detector, and then detectMotion.py

  

