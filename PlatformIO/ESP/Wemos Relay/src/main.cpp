#include <Arduino.h>

void setup()
{
  // initialize digital pin LED_BUILTIN as an output.
  Serial.println("Gestartet");
  Serial.begin(9600);
  pinMode(4, OUTPUT);
  pinMode(A0, INPUT);
}

// the loop function runs over and over again forever
void loop()
{
  int sensorWert = analogRead(A0); // Auslesen des aktuellen Sensorwertes
  Serial.println(sensorWert);      // Ausgabe des Wertes
  delay(50);
  if (sensorWert > 500)
  {
    digitalWrite(4, LOW);
    Serial.println("Low");
    delay(5000);
  }
  else
  {
    digitalWrite(4, HIGH);
    Serial.println("High");
    delay(2000);
  }
}
