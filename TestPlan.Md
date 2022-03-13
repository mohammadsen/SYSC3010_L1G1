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
<img width="673" alt="Screen Shot 2022-03-12 at 9 20 21 PM" src="https://user-images.githubusercontent.com/15981590/158042092-6095358b-73e9-4b92-bb35-c51cd2fb5357.png">

