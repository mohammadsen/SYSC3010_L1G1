/* *
 * This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK (v2).
 * Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
 * session persistence, api calls, and more.
 * */
const Alexa = require('ask-sdk-core');
const firebase = require('firebase/app');
require('firebase/database');

const config = {
  apiKey: "AIzaSyCjM2ldLom7MMcyHelKZoOxyMz0sJBbLeQ",
  authDomain: "l1g1finalfirebase.firebaseapp.com",
  databaseURL: "https://l1g1finalfirebase-default-rtdb.firebaseio.com",
  projectId: "l1g1finalfirebase",
  storageBucket: "l1g1finalfirebase.appspot.com",
  messagingSenderId: "612873609529",
  appId: "1:612873609529:web:1918fdaf223e6cfdde08e8",
  measurementId: "G-Z1K9T2GG39",
};

firebase.initializeApp(config);
const database = firebase.database();


const LaunchRequestHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'LaunchRequest';
    },
    handle(handlerInput) {
        const speakOutput = 'Welcome, you can say Hello or Help. Which would you like to try?';

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};


const LightOnIntentHandler = {
    
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'LightOn';
    },
   
    async handle(handlerInput) {
        let speakOutput = "Turning LED Strip On";
        try{
           
            firebase.database().goOnline();
            console.log("Connected\n");
            await firebase.database().ref("LedStatus").update({
            'LedStatus': 1, 
            'LedEffect': 1,
            });
            
            firebase.database().goOffline();
        
        }catch(e){
            console.log("Catch logs here: ",e);
            speakOutput = `There was a problem adding `;
        }
        console.log("Out of Try Catch");
        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

const LightOffIntentHandler = {
    
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'LightOff';
    },
   
    async handle(handlerInput) {
       let speakOutput = "Turning LED Strip Off";
        try{
           
            firebase.database().goOnline();
            console.log("Connected\n");
            await firebase.database().ref("LedStatus").update({
            'LedStatus': 0, 
            'LedEffect': 0,
            });
            
            firebase.database().goOffline();
        
        }catch(e){
            console.log("Catch logs here: ",e);
            speakOutput = `There was a problem adding `;
        }
        console.log("Out of Try Catch");
        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

const LightsRedIntentHandler = {
    
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'LightsRed';
    },
   
    async handle(handlerInput) {
        let speakOutput = "Changing LED Strip to Red";
        try{
           
            firebase.database().goOnline();
            console.log("Connected\n");
            await firebase.database().ref("LedStatus").update({
            'LedStatus': 1, 
            'LedEffect': 2,
            });
            
            firebase.database().goOffline();
        
        }catch(e){
            console.log("Catch logs here: ",e);
            speakOutput = `There was a problem adding `;
        }
        console.log("Out of Try Catch");
        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

const LightsGreenIntentHandler = {
    
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'LightsGreen';
    },
   
    async handle(handlerInput) {
        let speakOutput = "Changing LED Strip to Green";
        try{
           
            firebase.database().goOnline();
            console.log("Connected\n");
            await firebase.database().ref("LedStatus").update({
            'LedStatus': 1, 
            'LedEffect': 3,
            });
            
            firebase.database().goOffline();
        
        }catch(e){
            console.log("Catch logs here: ",e);
            speakOutput = `There was a problem adding `;
        }
        console.log("Out of Try Catch");
        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

const LightsBlueIntentHandler = {
    
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'LightsBlue';
    },
   
    async handle(handlerInput) {
        let speakOutput = "Changing LED Strip to Blue";
        try{
           
            firebase.database().goOnline();
            console.log("Connected\n");
            await firebase.database().ref("LedStatus").update({
            'LedStatus': 1, 
            'LedEffect': 4,
            });
            
            firebase.database().goOffline();
        
        }catch(e){
            console.log("Catch logs here: ",e);
            speakOutput = `There was a problem adding `;
        }
        console.log("Out of Try Catch");
        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

const LightsYellowIntentHandler = {
    
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'LightsYellow';
    },
   
    async handle(handlerInput) {
        let speakOutput = "Changing LED Strip to Yellow";
        try{
           
            firebase.database().goOnline();
            console.log("Connected\n");
            await firebase.database().ref("LedStatus").update({
            'LedStatus': 1, 
            'LedEffect': 5,
            });
            
            firebase.database().goOffline();
        
        }catch(e){
            console.log("Catch logs here: ",e);
            speakOutput = `There was a problem adding `;
        }
        console.log("Out of Try Catch");
        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

const LightsOrangeIntentHandler = {
    
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'LightsOrange';
    },
   
    async handle(handlerInput) {
        let speakOutput = "Changing LED Strip to Orange";
        try{
           
            firebase.database().goOnline();
            console.log("Connected\n");
            await firebase.database().ref("LedStatus").update({
            'LedStatus': 1, 
            'LedEffect': 6,
            });
            
            firebase.database().goOffline();
        
        }catch(e){
            console.log("Catch logs here: ",e);
            speakOutput = `There was a problem adding `;
        }
        console.log("Out of Try Catch");
        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

const LightsIndigoIntentHandler = {
    
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'LightsIndigo';
    },
   
    async handle(handlerInput) {
        let speakOutput = "Changing LED Strip to Indigo";
        try{
           
            firebase.database().goOnline();
            console.log("Connected\n");
            await firebase.database().ref("LedStatus").update({
            'LedStatus': 1, 
            'LedEffect': 7,
            });
            
            firebase.database().goOffline();
        
        }catch(e){
            console.log("Catch logs here: ",e);
            speakOutput = `There was a problem adding `;
        }
        console.log("Out of Try Catch");
        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

const LightsRoseIntentHandler = {
    
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'LightsRose';
    },
   
    async handle(handlerInput) {
        let speakOutput = "Changing LED Strip to Rose";
        try{
           
            firebase.database().goOnline();
            console.log("Connected\n");
            await firebase.database().ref("LedStatus").update({
            'LedStatus': 1, 
            'LedEffect': 8,
            });
            
            firebase.database().goOffline();
        
        }catch(e){
            console.log("Catch logs here: ",e);
            speakOutput = `There was a problem adding `;
        }
        console.log("Out of Try Catch");
        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

const LightsWhiteIntentHandler = {
    
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'LightsWhite';
    },
   
    async handle(handlerInput) {
        let speakOutput = "Changing LED Strip to White";
        try{
           
            firebase.database().goOnline();
            console.log("Connected\n");
            await firebase.database().ref("LedStatus").update({
            'LedStatus': 1, 
            'LedEffect': 1,
            });
            
            firebase.database().goOffline();
        
        }catch(e){
            console.log("Catch logs here: ",e);
            speakOutput = `There was a problem adding `;
        }
        console.log("Out of Try Catch");
        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

const LightsCyanIntentHandler = {
    
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'LightsCyan';
    },
   
    async handle(handlerInput) {
        let speakOutput = "Changing LED Strip to Cyan";
        try{
           
            firebase.database().goOnline();
            console.log("Connected\n");
            await firebase.database().ref("LedStatus").update({
            'LedStatus': 1, 
            'LedEffect': 9,
            });
            
            firebase.database().goOffline();
        
        }catch(e){
            console.log("Catch logs here: ",e);
            speakOutput = `There was a problem adding `;
        }
        console.log("Out of Try Catch");
        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

const HelloWorldIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'HelloWorldIntent';
    },
    handle(handlerInput) {
        const speakOutput = 'Hello World!';

        return handlerInput.responseBuilder
            .speak(speakOutput)
            //.reprompt('add a reprompt if you want to keep the session open for the user to respond')
            .getResponse();
    }
};

const HelpIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.HelpIntent';
    },
    handle(handlerInput) {
        const speakOutput = 'You can say hello to me! How can I help?';

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

const CancelAndStopIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && (Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.CancelIntent'
                || Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.StopIntent');
    },
    handle(handlerInput) {
        const speakOutput = 'Goodbye!';

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .getResponse();
    }
};
/* *
 * FallbackIntent triggers when a customer says something that doesn’t map to any intents in your skill
 * It must also be defined in the language model (if the locale supports it)
 * This handler can be safely added but will be ingnored in locales that do not support it yet 
 * */
const FallbackIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'AMAZON.FallbackIntent';
    },
    handle(handlerInput) {
        const speakOutput = 'Sorry, I don\'t know about that. Please try again.';

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};
/* *
 * SessionEndedRequest notifies that a session was ended. This handler will be triggered when a currently open 
 * session is closed for one of the following reasons: 1) The user says "exit" or "quit". 2) The user does not 
 * respond or says something that does not match an intent defined in your voice model. 3) An error occurs 
 * */
const SessionEndedRequestHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'SessionEndedRequest';
    },
    handle(handlerInput) {
        console.log(`~~~~ Session ended: ${JSON.stringify(handlerInput.requestEnvelope)}`);
        // Any cleanup logic goes here.
        return handlerInput.responseBuilder.getResponse(); // notice we send an empty response
    }
};
/* *
 * The intent reflector is used for interaction model testing and debugging.
 * It will simply repeat the intent the user said. You can create custom handlers for your intents 
 * by defining them above, then also adding them to the request handler chain below 
 * */
const IntentReflectorHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest';
    },
    handle(handlerInput) {
        const intentName = Alexa.getIntentName(handlerInput.requestEnvelope);
        const speakOutput = `You just triggered ${intentName}`;

        return handlerInput.responseBuilder
            .speak(speakOutput)
            //.reprompt('add a reprompt if you want to keep the session open for the user to respond')
            .getResponse();
    }
};
/**
 * Generic error handling to capture any syntax or routing errors. If you receive an error
 * stating the request handler chain is not found, you have not implemented a handler for
 * the intent being invoked or included it in the skill builder below 
 * */
const ErrorHandler = {
    canHandle() {
        return true;
    },
    handle(handlerInput, error) {
        const speakOutput = 'Sorry, I had trouble doing what you asked. Please try again.';
        console.log(`~~~~ Error handled: ${JSON.stringify(error)}`);

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

/**
 * This handler acts as the entry point for your skill, routing all request and response
 * payloads to the handlers above. Make sure any new handlers or interceptors you've
 * defined are included below. The order matters - they're processed top to bottom 
 * */
exports.handler = Alexa.SkillBuilders.custom()
    .addRequestHandlers(
        LaunchRequestHandler,
        HelloWorldIntentHandler,
        LightOnIntentHandler,
        LightOffIntentHandler,
        LightsCyanIntentHandler,
        LightsWhiteIntentHandler,
        LightsRoseIntentHandler,
        LightsIndigoIntentHandler,
        LightsOrangeIntentHandler,
        LightsYellowIntentHandler,
        LightsBlueIntentHandler,
        LightsGreenIntentHandler,
        LightsRedIntentHandler,
        HelpIntentHandler,
        CancelAndStopIntentHandler,
        FallbackIntentHandler,
        SessionEndedRequestHandler,
        IntentReflectorHandler)
    .addErrorHandlers(
        ErrorHandler)
    .withCustomUserAgent('sample/hello-world/v1.2')
    .lambda();