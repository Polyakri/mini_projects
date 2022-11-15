#include <SoftwareSerial.h>
#include "I2Cdev.h"
#include "MPU6050.h"
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    #include "Wire.h"
#endif

MPU6050 accelgyro;
int16_t ax, ay, az;
int16_t gx, gy, gz;

#define OUTPUT_READABLE_ACCELGYRO

//Assign Variables to ports to make the code easier

//Speed Indication Leds
int ZeroSpeed=5;
int LowSpeed=4;
int MediumSpeed=3;
int HighSpeed=15;

//Forward or Reverse Leds
int ForwardLed=14;
int ReverseLed=16;

//Start and Stop Buttons
int StartButton=8;
int StopButton=9;

//Forward or Reverse Buttons
int ForwardButton=7;
int ReverseButton=6;

//Speed Up & Down Buttons
int SpeedUp=13;
int SpeedDown=12;


//Declare Some other Useful Variables

//Button State and previous Button states to see if a button is pressed 
int PrevStartButtonState=0;
int StartButtonState=0;

int PrevStopButtonState=0;
int StopButtonState=0;

int PrevForwardButtonState=0;
int ForwardButtonState=0;

int PrevReverseButtonState=0;
int ReverseButtonState=0;

int PrevSpeedUpState=0;
int SpeedUpState=0;

int PrevSpeedDownState=0;
int SpeedDownState=0;

//SomeFlags
int ForwardReverse=1; //If this is 1 it goes Forward, if it is 0 it goes Reverse , Default is Forward
int Speed=0;  //Stop =0 , Low Speed =1 , Medium Speed = 2 , HighSpeed = 3 , On App Start is is 0, On start press is 1, on stop is 0  
unsigned long prevTime=millis();
//Bluetooth Setup Pins
SoftwareSerial BTserial(10, 11);
//setup function runs at start once
void setup() {
  //setup led as outputs
  pinMode (ZeroSpeed, OUTPUT);
  pinMode (LowSpeed,OUTPUT);
  pinMode (MediumSpeed,OUTPUT);
  pinMode (HighSpeed,OUTPUT);
  pinMode (ForwardLed,OUTPUT);
  pinMode (ReverseLed,OUTPUT);

  //setup button as inputs 
  pinMode (StartButton, INPUT);
  pinMode (StopButton, INPUT);
  pinMode (ForwardButton, INPUT);
  pinMode (ReverseButton, INPUT);
  pinMode (SpeedUp,INPUT);
  pinMode (SpeedDown,INPUT);

  //setup Bluetooth
  BTserial.begin(9600);

  Wire.begin();
   accelgyro.initialize();
}


//main code that runs on loop
void loop() {
 accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
unsigned long currTime=millis();

//read Inputs
StartButtonState=digitalRead (StartButton);
StopButtonState=digitalRead (StopButton);
ForwardButtonState=digitalRead (ForwardButton);
ReverseButtonState=digitalRead (ReverseButton);
SpeedUpState=digitalRead (SpeedUp);
SpeedDownState=digitalRead (SpeedDown);

//Check if the Button went from Low to High, but we need to do it once. That is the reason the below code is used
if (StartButtonState!=PrevStartButtonState){
  if(StartButtonState==HIGH){
    if(Speed==0){ //If it is Stopped Start is 
    Speed=1;
    }
  }
}

if (StopButtonState!=PrevStopButtonState){
  if(StopButtonState==HIGH){
    Speed=0;
  }
}

if (ForwardButtonState!=PrevForwardButtonState){
  if(ForwardButtonState==HIGH){
    ForwardReverse=1;
  }
}

if (ReverseButtonState!=PrevReverseButtonState){
  if(ReverseButtonState==HIGH){
    ForwardReverse=0;
  }
}

if (SpeedUpState!=PrevSpeedUpState){
  if(SpeedUpState==HIGH){
    if(Speed!=0 && Speed < 3 ){
      Speed=Speed+1;
    }
  }
}

if (SpeedDownState!=PrevSpeedDownState){
  if(SpeedDownState==HIGH){
     if(Speed!=0 && Speed > 1 ){
      Speed=Speed-1;
    }
  }
}

PrevStartButtonState=StartButtonState;
PrevStopButtonState=StopButtonState;
PrevForwardButtonState=ForwardButtonState;
PrevReverseButtonState=ReverseButtonState;
PrevSpeedUpState=SpeedUpState;
PrevSpeedDownState=SpeedDownState; 

//Display on the Leds
if(Speed==0){
  digitalWrite(ZeroSpeed ,HIGH);
  digitalWrite(LowSpeed ,LOW);
  digitalWrite(MediumSpeed ,LOW);
  digitalWrite(HighSpeed ,LOW);
}else if (Speed==1){
  digitalWrite(ZeroSpeed ,LOW);
  digitalWrite(LowSpeed ,HIGH);
  digitalWrite(MediumSpeed ,LOW);
  digitalWrite(HighSpeed ,LOW);
}else if (Speed==2){
  digitalWrite(ZeroSpeed ,LOW);
  digitalWrite(LowSpeed ,LOW);
  digitalWrite(MediumSpeed ,HIGH);
  digitalWrite(HighSpeed ,LOW);
}else {
  digitalWrite(ZeroSpeed ,LOW);
  digitalWrite(LowSpeed ,LOW);
  digitalWrite(MediumSpeed ,LOW);
  digitalWrite(HighSpeed ,HIGH);
}

if(ForwardReverse==1){
  digitalWrite(ForwardLed,HIGH);
  digitalWrite(ReverseLed,LOW); 
}else{
  digitalWrite(ForwardLed,LOW);
  digitalWrite(ReverseLed,HIGH); 
}

if(currTime-prevTime>100){
  float degree=grpar(ax);
//  BTserial.print (degree);
//BTserial.print (' ' );
 // BTserial.print (Speed);
//BTserial.print (' ' );
//BTserial.print (ForwardReverse);
//BTserial.print (' ' );
BTserial.println(allinoneint(degree,Speed,ForwardReverse));

prevTime=millis();

}



delay (20); //Avoid some bouncing effects 

}

float grpar(float var){
  float deg;
  float temp = 0.0055*(var+15500);
  if(temp<95 && temp >85){
    temp=90;
  }
   
   if(temp>180){
    temp=180;
   }
   if(temp<0){
    temp=0;
   }
   deg=round_fun(temp);
   
  return deg;
}

float round_fun (float var){
  float value = (int)(var * 100 + .5); 
    return (float)value / 100;
}

long int allinoneint (float degree, int Speed, int ForwardReverse){
 long int retVal=degree*10000+10*Speed+ForwardReverse;
  return retVal;
}
