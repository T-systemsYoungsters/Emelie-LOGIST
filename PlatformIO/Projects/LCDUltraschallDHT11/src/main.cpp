#include <Arduino.h>
#include "DHT.h"
#include <LiquidCrystal.h>
#include <Wire.h>
#define DHTPIN 7
#define DHTTYPE DHT11
int trigger = 9;
int echo = 8;
long dauer = 0;
long entfernung = 0;
const int rs = 12, en = 13, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

DHT dht(DHTPIN, DHTTYPE);

void setup()
{
  Serial.begin(9600);
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  lcd.begin(16, 2);
  Serial.begin(9600);
  lcd.println("DHT11 Testprogramm");
  dht.begin();
}

void loop()

{
  digitalWrite(trigger, LOW);
  delay(5);
  digitalWrite(trigger, HIGH);
  delay(10);
  digitalWrite(trigger, LOW);
  dauer = pulseIn(echo, HIGH);
  entfernung = (dauer / 2) / 29.1;
  lcd.print(entfernung);
  lcd.println("cm");
  delay(1000);
  // lcd.setCursor(0, 1);
  // lcd.print(millis() / 1000);
  delay(2000);

  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (isnan(h) || isnan(t))
  {
    Serial.println("Fehler beim auslesen des Sensors!");
    return;
  }
  //lcd.print("Luftfeuchtigkeit: ");
  lcd.print(h);
  lcd.print("%\t");
 // lcd.print("Temperatur: ");
  lcd.print(t);
  //lcd.write("°");
  //lcd.println("C");
}