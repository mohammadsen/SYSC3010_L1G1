#include <Arduino.h>
#include <FastLED.h>

#define LED_PIN 12 
#define NUM_LEDS 60
CRGB leds[NUM_LEDS];


// the setup function runs once when you press reset or power the board
void setup() {

  Serial.print("Testing");
  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setMaxPowerInVoltsAndMilliamps(5, 500);
  FastLED.clear();
  FastLED.show();

}


void makeLightEffect(int input){
  if (input == 1){
    for (int i=0; i<NUM_LEDS; i++){
                leds[i] = CRGB(255,0,0);
                FastLED.setBrightness(2*i);
                FastLED.show();
                
              }
    
    }else if(input == 2){
      for (int i=0; i<NUM_LEDS; i++){
                leds[i] = CRGB(0,255,0 );
                FastLED.setBrightness(2*i);
                FastLED.show();
               
              }
      }else if(input == 3){
        for (int i=0; i<NUM_LEDS; i++){
                leds[i] = CRGB(0,0,255 );
                FastLED.setBrightness(2*i);
                FastLED.show();
              }}}
              
void loop() {
 
  delay(1000);
  makeLightEffect(1);
  delay(3000);
  makeLightEffect(2);
  delay(3000);
  makeLightEffect(3);
  delay(3000);
  
  
  

}
