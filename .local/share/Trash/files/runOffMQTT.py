import pwm0
import paho.mqtt.client as mqtt
import time

msg = ""

#on_connect to the MQTT server:
def on_connect(client,userdata,flags,rc):
    print("Connection resulted in: "+connack_string(rc))
    client.subscribe("blanotiger/movement") #subscribes upon connect
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
    if msg=="forward":
        msg=""
        forward()
        print("Forward.")
    elif msg=="backward":
        msg=""
        backward()
        print("Backward.")
    elif msg=="stop":
        msg=""
        stop()
        print("Stop.")


#This code will connect to the broker:
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect("test.mosquitto.org", 1883, 60) #Formatted (address, port, keepalive(seconds))

#This code will subscribe to a topic:
print("Subscribing to topic 'blanotiger/movement'...")
client.subscribe("blanotiger/movement",0)
print("Subscribed!")

client.loop_forever()
