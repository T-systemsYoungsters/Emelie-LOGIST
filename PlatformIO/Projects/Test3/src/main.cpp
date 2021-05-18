#include <Arduino.h>
#include <WiFi.h>
#include <WiFiClient.h>

const char* ssid = "WLAN-721926";
const char* password = "74381122415911764409";

void setup() {
  Serial.begin(115200);
  //delay(500);
  //pinMode(4, OUTPUT);
  WiFi.begin(ssid, password);  // Connect to WiFi network
    Serial.println("");
 
    while (WiFi.status() != WL_CONNECTED) // Wait for connection
   {
        delay(500);
        Serial.print(".");
    }
    Serial.println("");
    Serial.print("Connected to ");
    Serial.println(ssid);
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());

}

void loop() {
  //digitalWrite(4,HIGH);
  //Serial.println("ON");
  //delay(500);
  //digitalWrite(4,LOW);
  //Serial.println("OFF");
  //delay(500);
}