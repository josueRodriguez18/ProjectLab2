import pwm0 as pwm
import paho.mqtt.client as mqtt
import time
import gyro

flag = 0
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
        pwm.forward()
        print("Forward.")
    elif msg=="backward":
        msg=""
        pwm.backward()
        print("Backward.")
    elif msg=="stop":
	msg=""
	pwm.stop()
	flag = 0
        print("Stop.")
	client.publish("blanotiger/movement", payload=gyro.angle, qos=0,retain=False)
    elif msg=="forward left":
	msg=""
	pwm.forward_left()
	print("Forward Left.")
    elif msg=="forward right":
	msg=""
	pwm.forward_right()
	print("Forward Right.")
    elif msg=="spin":
	msg=""
	flag = 1
	pwm.spin()
	print("Spin")


#This code will connect to the broker:
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect("172.16.0.124", 1883, 60) #Formatted (address, port, keepalive(seconds))

#This code will subscribe to a topic:
print("Subscribing to topic 'blanotiger/robot2'...")
client.subscribe("blanotiger/robot2",0)
print("Subscribed!")

client.loop_forever()


