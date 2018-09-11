#include "WiFi.h"
#include "ArduinoJson.h"
char ssid[] = "TTU Swarm Field";
IPAddress ip(172,16,0,1);
String jData;

WiFiClient client;

void setup(){
    //connects to router
    WiFi.begin(ssid);
    while(WiFi.status() != WL_CONNECTED){
        delay(1000); Serial.print("Connecting to SSID..");
        //if not connected output connecting and try to connect again
        WiFi.begin(ssid);
    }
    client.connect(ip, 8001);
    //should be delted if memory becomes an issue
    while(!client.connected()){
        //if not connected to server output connecting and try to connect again
        delay(1000); Serial.print("Connecting to server..");
        client.connect(ip, 8001);
    };

}

void loop(){
    //poll server for field data
    client.write("%GET{FieldData}%");
    //while the buffer from the server isn't empty concatenate the bytes into one string
    while(client.available()){
        jData += client.read();

    }
    //alternative GET path needs testing
    //write('%GET{GetData}%');



}