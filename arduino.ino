#include <dht.h>

//#include "DHT.h"
#define dht_apin A0 
#define ldr A1
int sensor_pin = A2;
int output_value ;
int phpin = 3; 
 
dht DHT;
 
void setup(){
 
  Serial.begin(9600);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(3, INPUT);
  digitalWrite(A1, LOW);
  digitalWrite(A2, LOW);
  digitalWrite(3, LOW);
  delay(10);

}//end "setup()"
 
void loop(){
  //Start of Program 
int ph = digitalRead(3);
    output_value= analogRead(sensor_pin);
    output_value = map(output_value,550,0,0,100);
    DHT.read11(dht_apin);
    int sensorValue = analogRead(ldr);
    Serial.print(String (ph));
    Serial.print(","" ");
    Serial.print(String (output_value));
    Serial.print("!"" ");
    Serial.print(String (DHT.humidity));
    Serial.print("@"" ");
    Serial.print(String (DHT.temperature));
    Serial.print(";"" "); 
    Serial.println(String (sensorValue));
    delay(2000);
    
  
}
