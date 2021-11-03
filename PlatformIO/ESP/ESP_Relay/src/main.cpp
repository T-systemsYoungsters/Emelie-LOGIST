#include <Arduino.h>

void setup()
{
  // initialize digital pin LED_BUILTIN as an output.
  Serial.println("Gestartet");
  Serial.begin(115200);
  pinMode(4, OUTPUT);
}

// the loop function runs over and over again forever
void loop()
{
  //int sensorWert = analogRead(A0); // Auslesen des aktuellen Sensorwertes
  //Serial.println(sensorWert);      // Ausgabe des Wertes
  //delay(50);
  //if (sensorWert < 400)
  //{
    digitalWrite(16, HIGH);
    Serial.println("High");
    delay(5000);
  //}
  //else
  //{
    digitalWrite(16, LOW);
    Serial.println("Low");
    delay(2000);
  //}
}

