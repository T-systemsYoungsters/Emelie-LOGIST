#include <Arduino.h>
void setup() {
 Serial.begin(9600);               // Start der seriellen Kommunikation
 Serial.println("Gestartet");
  pinMode(13, OUTPUT);
  pinMode(A0, INPUT);
  
}

void loop() {
 int sensorWert = analogRead(A0);  // Auslesen des aktuellen Sensorwertes
 Serial.println(sensorWert);       // Ausgabe des Wertes
 delay(50);                       // kurze Pause
 if (sensorWert < 400) 
 {
  digitalWrite(13, HIGH);
  delay(5000);
 }
 else
 {
  digitalWrite(13, LOW);
  delay(2000);
 }
}