#include <Arduino.h>

void setup() {
 // pinMode(13, OUTPUT);
  Serial.begin(9600);               // Start der seriellen Kommunikation
}

void loop() {
  int sensorWert = analogRead(A1);  // Auslesen des aktuellen Sensorwertes
  Serial.println(sensorWert);       // Ausgabe des Wertes 
   delay(50)                    // kurze Pause
 // digitalWrite(13, HIGH);
  //delay(5000);
  //digitalWrite(13, LOW);
  //delay(2000);
}