#include <Arduino.h>

void setup() {
  // put your setup code here, to run once:
  pinMode(8,OUTPUT);
  


}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(13,HIGH);
  delay(500);
  digitalWrite(13,LOW);
  delay(500);
}
