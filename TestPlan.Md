# Test Plan for L1G1 


### This is the test plan that is used to test our End to End communication portion of the Project. 
### In order to Verify that most of these tests work, you must be logged into the Firebase Console. 

# Alexa: 
In order to test that the Alexa, you must be logged into the Amazon Alexa Developer Dashboard @ developer.amazon.com/dashboard

1.) Either Enter or Speak "Tell light control to turn on lights"  -> The value that should be observed in Firebase is: LedStatus/LedStatus: 1

2.) Either Enter or Speak "Tell light control to turn off light strip"  -> The value that should be observed in Firebase is:  LedStatus/LedStatus: 0

# GUI Test

### To Test The GUI, You must download and Open Index.html in your desired Browser. It found in the Github Repo

1.) In the GUI, Click the "Turn on" button  -> The value that should be observed in Firebase is: LedStatus/LedStatus: 1;

2.) In the GUI, Click the "Turn off" button  -> The value that should be observed in Firebase is: LedStatus/LedStatus: 0;

In both cases, you can further verify that the GUI buttons are working by looking at the Web Browsers Console. 

The Console should Display this: 

[Log] I sensed a click (index.html, line 82)

[Log] Connected (index.html, line 84)

[Log] The value has been Updated & The Light is OFF (index.html, line 89)

# Motion Sensor 









# Deployment Diagram


# Communication Protocol Table

# Sender	Receiver	Message	Data Format	Purpose
Raspberry Pi	Firebase	detectsMotion()	Boolean (0 or 1) 	Notifies Firebase motion is detected
Raspberry Pi (Alexa)	Firebase	firebase.database().ref("LedStatus").set{}	Boolean (0 or 1)	Turns Lights on or Off
Raspberry Pi (Alexa)	Firebase	firebase.database().ref("LedEffect").set{}	Boolean (0 to 9)	Sets LED Effects
ESP 32	LED	makeLightEffect()	Int (0 to 11)	Controls LED lights; 0 & 1 are used to turn off and on lights
GUI	Firebase	TurnOnLight()	Boolean(0 or 1) 	Used to Turn on Light; Base Color is White
GUI	Firebase 	TurnOffLight()	Boolean(0 or 1) 	Used to turn off light
GUI	Firebase	SetLightEffect(x)	Int(0 to 9)	Used for different light effects
Firebase	ESP32	Firebase.RTDB.getInt(&fbdo, "/LedStatus/LedStatus")	Boolean (0 or 1) 	Determines if light is on
Firebase	ESP32	Firebase.RTDB.getInt(&fbdo, "/LedStatus/Ledeffect")	Int (1 – 9)	Sets Light Effect

