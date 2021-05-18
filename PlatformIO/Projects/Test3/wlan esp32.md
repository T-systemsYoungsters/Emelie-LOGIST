#include <WiFi.h>
#include <WiFiClient.h>
 
const char* ssid = "ESP32-Server";
const char* password = "-----------";
 
void setup(void)
{  
    Serial.begin(115200);    
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
 
void loop(void)
{
}