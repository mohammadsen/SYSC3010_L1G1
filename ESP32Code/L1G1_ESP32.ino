//SYSC3010 L1G1 ESP 32 Code 
//This code makes the ESP32 communicate with the Firebase Realtime Database and Control the LED strip
//@Author Mohammad Gaffori


#include <Arduino.h>
#include <WiFi.h>
#include <Firebase_ESP_Client.h>
#include <FastLED.h>

//Declating Constants
#define LED_PIN 12 
#define NUM_LEDS 60
CRGB leds[NUM_LEDS];


//Token Generation for FireBase Access
#include "addons/TokenHelper.h"
//RealTime Database Helper + Addons 
#include "addons/RTDBHelper.h"

// Wifi Credentials 
#define WIFI_SSID "The House"
#define WIFI_PASSWORD "Carleton77"

//#define WIFI_SSID "Testing"
//#define WIFI_PASSWORD "password"

// Firebase Project API Key 
#define API_KEY "AIzaSyCjM2ldLom7MMcyHelKZoOxyMz0sJBbLeQ"

//Firebase DataBase URL 
#define DATABASE_URL "https://l1g1finalfirebase-default-rtdb.firebaseio.com/" 

//Define Firebase Data objects
FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config;

// Defining Variables Required to Interact With Firebase 
unsigned long sendDataPrevMillis = 0;
int intValue;
float floatValue;
bool signupOK = false;

//Counter Used for MotionDetector 
int motionCount; 

void setup() {

  //Connecting to FastLED (LED Strip Conroller)
  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setMaxPowerInVoltsAndMilliamps(5, 500);
  FastLED.clear();
  FastLED.show();

  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(300);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  // Configuring Firebase Credentials 
  config.api_key = API_KEY;
  config.database_url = DATABASE_URL;

  //Connecting to FireBase
  if (Firebase.signUp(&config, &auth, "", "")) {
    Serial.println("ok");
    signupOK = true;
  }
  else {
    Serial.printf("%s\n", config.signer.signupError.message.c_str());
  }

  //Assign the callback function for the long running token generation task 
  config.token_status_callback = tokenStatusCallback; 
  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);

}

//Function that is called when Motion is Detected and LightStrips are off
void motionDetectedOn(){
  Firebase.RTDB.setInt(&fbdo, "/LedStatus/LedStatus", 1);
  Firebase.RTDB.setInt(&fbdo, "/LedStatus/LedEffect", 1);
  Firebase.RTDB.setInt(&fbdo, "/Motion/Motion detected", 0);
  motionCount = 1;    //Set motion counter to 1
  }

//Function that is called when Motion is Detected and LightStrips are on
void motionDetectedOff(){
  Firebase.RTDB.setInt(&fbdo, "/LedStatus/LedStatus", 0);
  Firebase.RTDB.setInt(&fbdo, "/LedStatus/LedEffect", 0);
  Firebase.RTDB.setInt(&fbdo, "/Motion/Motion detected", 0);
  motionCount = 0;  //Set motion counter to 0
  }
  
//Function that controls the light strip effect depending on User Selection  
void makeLightEffect(int input){
  if (input == 1){
    for (int i=0; i<NUM_LEDS; i++){
                leds[i] = CRGB(255,255,255);
                FastLED.setBrightness(2*i);
                FastLED.show();
                delay(50);
              }
    
    }else if(input == 2){
      for (int i=0; i<NUM_LEDS; i++){
                leds[i] = CRGB(255,0,0 );
                FastLED.setBrightness(2*i);
                FastLED.show();
                delay(50);
              }
      }else if(input == 3){
        for (int i=0; i<NUM_LEDS; i++){
                leds[i] = CRGB(0,255,0 );
                FastLED.setBrightness(2*i);
                FastLED.show();
                delay(50);
              }
      }else if(input == 4){
        for (int i=0; i<NUM_LEDS; i++){
                leds[i] = CRGB(0,0,255 );
                FastLED.setBrightness(2*i);
                FastLED.show();
                delay(50);
              }
      }else if(input == 5){
        for (int i=0; i<NUM_LEDS; i++){
                leds[i] = CRGB(255,255,0 );
                FastLED.setBrightness(2*i);
                FastLED.show();
                delay(50);
              }
      }else if(input == 6){
        for (int i=0; i<NUM_LEDS; i++){
                leds[i] = CRGB(255,128,0 );
                FastLED.setBrightness(2*i);
                FastLED.show();
                delay(50);
              }
      }else if(input == 7){
        for (int i=0; i<NUM_LEDS; i++){
                leds[i] = CRGB(75,0,130 );
                FastLED.setBrightness(2*i);
                FastLED.show();
                delay(50);
              }
      }else if(input == 8){
        for (int i=0; i<NUM_LEDS; i++){
                leds[i] = CRGB(243,196,297 );
                FastLED.setBrightness(2*i);
                FastLED.show();
                delay(50);
              }
      }else if(input == 9){
        for (int i=0; i<NUM_LEDS; i++){
                leds[i] = CRGB(0,255,255);
                FastLED.setBrightness(2*i);
                FastLED.show();
                delay(50);
              }
      }
     
  }

void loop() {
  

  if (Firebase.ready() && signupOK && (millis() - sendDataPrevMillis > 3000 || sendDataPrevMillis == 0)) { //If firebase Connection okay & 3 seconds have passed
    sendDataPrevMillis = millis();

    //If motion Detected and Light Strip is off, call motionDetectedOn() to turn on light strip
    if (Firebase.RTDB.getInt(&fbdo, "/Motion/Motion detected")  && fbdo.intData() == 1) {
        motionDetectedOn();
        //If motion Detected and Light Strip is on, with motion counter set to true call motionDetectedOff();
      } else if (Firebase.RTDB.getInt(&fbdo, "/Motion/Motion detected")  && fbdo.intData() == 1 && motionCount == 1){
        motionDetectedOff();
      }
      
    if (Firebase.RTDB.getInt(&fbdo, "/LedStatus/LedStatus")  && fbdo.intData() == 1) { //If ledStatus is 1 on Firebase
      for (int i=1;i<10; i++){ 
        if (Firebase.RTDB.getInt(&fbdo, "/LedStatus/LedEffect")  && fbdo.intData() == i) { //If for loop value matches Firebase value
           makeLightEffect(i); //Makelighteffect of user selected value
           Serial.println("Changed");
           break;
          }
        }
      }
    }else {
       Serial.println(fbdo.errorReason()); //else Stay on 
      for (int i=NUM_LEDS; i>=0; i--){
          leds[i] = CRGB(0,0 , 0);
          FastLED.setBrightness(100-i);
          FastLED.show();
          delay(50);
        }
      }
  }
