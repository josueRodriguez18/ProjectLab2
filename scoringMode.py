#Libraries
import paho.mqtt.client as mqtt
import json
import requests
import time

msg = ""

def phase1():
    print("phase1()")
    r = requests.get('http://172.16.0.1:8001/FieldData/GetData')
    parsed = json.loads(r.text)
    print("Parsed.")
    info1 = parsed["Ball"]["Object Center"]['X']
    info2 = parsed["Ball"]["Object Center"]['Y']
    print("1")
    info3 = parsed["Blue Team Data"]["Circle"]["Object Center"]['X']
    info4 = parsed["Blue Team Data"]["Circle"]["Object Center"]['Y']
    print("2")
    client.publish("blanotiger/robot1",payload=("["+str(info1)+"]["+str(info2)+"]["+str(info3)+"]["+str(info4)+"]"),qos=1,retain=True) #This is formatted (topic,message)
    print("3")

def phase2():
    print("phase2()")
    r = requests.get('http://172.16.0.1:8001/FieldData/GetData')
    parsed = json.loads(r.text)
    print("Parsed.")
    info1 = parsed["Ball"]["Object Center"]['X']
    info2 = parsed["Ball"]["Object Center"]['Y']
    print("1")
    info3 = parsed["Blue Team Data"]["Triangle"]["Object Center"]['X']
    info4 = parsed["Blue Team Data"]["Triangle"]["Object Center"]['Y']
    print("2")
    client.publish("blanotiger/robot3",payload=("["+str(info1)+"]["+str(info2)+"]["+str(info3)+"]["+str(info4)+"]"),qos=1,retain=True) #This is formatted (topic,message)
    print("3")

def checkForStop():
    check = 22.0
    while check>21.0:
        r = requests.get('http://172.16.0.1:8001/FieldData/GetData')
        parsed = json.loads(r.text)
        print(str(parsed["Blue Team Data"]["Triangle"]["Object Center"]['X']))
        check = float(parsed["Blue Team Data"]["Triangle"]["Object Center"]['X'])
        time.sleep(1)

#on_connect to the MQTT server:
def on_connect(client,userdata,flags,rc):
    print("Connection resulted in: "+connack_string(rc))
    client.subscribe("blanotiger/fin") #subscribes upon connect
#on_disconnect to the MQTT server:    
def on_disconnect(client,userdata,rc):
    if rc!= 0:
        print("Unexpected disconnection.")
        client.reconnect()
#on_message from the MQTT server:        
def on_message(client,userdata,message):
    message.payload = message.payload.decode("utf-8")
    print("Received message '"+str(message.payload)+"' on topic '"+message.topic+"'.")
    msg = str(message.payload)
    if msg=="start":
        msg=""
        print("'Start' command received.")
        phase1()
        print("Phase 1 activated.")
    elif msg=="Bot 1 Complete":
        msg=""
        phase2()
        print("Phase 2 activated.")
    elif msg=="Bot 3 Complete":
        msg=""
        checkForStop()

#This code will connect to the broker:
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect("172.16.0.124", 1883, 60) #Formatted (address, port, keepalive(seconds))

print("Subscribing to topic 'blanotiger/fin'...")
client.subscribe("blanotiger/fin",0)
print("Subscribed!")

client.loop_forever()
