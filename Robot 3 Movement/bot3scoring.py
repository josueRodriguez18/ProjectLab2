import rotateFunction as gyro
import encoder as str8
import pwm0 as pwm
import paho.mqtt.client as mqtt
import math
import time
import json
import requests

msg = ""
botX = 0
botY = 0
ballX = 0
ballY = 0
midpointX = 0
midpointY = 0
theta = 0
phase = 0
getPath = "http://192.168.137.1:8001/FieldData/GetData"

def readIn(message):
    new = message
    i=0
    k=0
    q=[str(1),str(1),str(1),str(1)]
    count=0
    m=0
    while (count < 4):
        if (new[i] == "["):
            s=[]
            i=i+1
            j=i
            while (new[i] != "]"):
                i=i+1
            count=count+1
            m=i
            q[k]=str(new[j:m])
            k=k+1
            i=i+1
    global botX
    global botY
    global ballX
    global ballY
    botX = float(q[0])
    botY = float(q[1])
    ballX = float(q[2])
    ballY = float(q[3])

def findTheta():
    global theta
    global ballX
    global ballY
    x2 = ballX
    y2 = ballY
    adj = x2-4
    opp = 124-y2
    theta = math.tan(opp/adj) #returns value in radians

def findMid():
    global ballY
    global ballX
    global botY
    global theta
    y1 = botY
    y2 = ballY
    x2 = ballX
    adj = y1-y2
    arctan = math.atan(theta)
    opp = -(adj*arctan)
    global midpointX
    global midpointY
    midpointX = x2 + opp
    midpointY = y1
    client.publish("blanotiger/debug",payload="midpoint: ("+str(midpointX)+","+str(midpointY)+")",qos=0,retain=False)

def driveF():
    global phase
    client.publish("blanotiger/debug",payload="driveF("+str(phase)+") called.",qos=0,retain=False)
    global midpointX
    global botX
    global botY
    global ballY
    global ballX
    newparsed = ' '
    if phase == 1:
        while botX > midpointX:
            str8.forward(10)
	    pwm.stop()
	    time.sleep(0.5)
	    oldparsed = newparsed
            r = requests.get(getPath, timeout=2)
            parsed = json.loads(r.text)
	    newparsed = parsed["Blue Team Data"]["Triangle"]["Object Center"]["X"]
	    while oldparsed==newparsed:
		print("Data did not update.")
		client.publish("blanotiger/debug",payload="Data didn't update.",qos=0,retain=False)
		time.sleep(0.5)
		r = requests.get(getPath, timeout=2)
		parsed = json.loads(r.text)
		newparsed = parsed["Blue Team Data"]["Triangle"]["Object Center"]["X"]
            botX = float(parsed["Blue Team Data"]["Triangle"]["Object Center"]["X"])
	    client.publish("blanotiger/debug",payload="X: "+str(botX),qos=0,retain=False)
            print("botX: "+str(botX))
        print("Stopping...")
	client.publish("blanotiger/debug",payload="Movement 1 Complete.",qos=0,retain=False)
    elif phase == 2:
        str8.forward(10)
	while (botX >= ballX)or(botY >= ballY):
	    time.sleep(0.5)
            oldparsed = newparsed
            r = requests.get(getPath, timeout=2)
            parsed = json.loads(r.text)
            newparsed = parsed["Blue Team Data"]["Triangle"]["Object Center"]["X"]
            while oldparsed==newparsed:
                print("Data did not update.")
		client.publish("blanotiger/debug",payload="Data didn't update.",qos=0,retain=False)
                time.sleep(0.5)
                r = requests.get(getPath, timeout=2)
                parsed = json.loads(r.text)
                newparsed = parsed["Blue Team Data"]["Triangle"]["Object Center"]["X"]
            botX = float(parsed["Blue Team Data"]["Triangle"]["Object Center"]["X"])
            botY = float(parsed["Blue Team Data"]["Triangle"]["Object Center"]["Y"])
            client.publish("blanotiger/debug",payload="Bot: ("+str(botX)+","+str(botY)+")",qos=0,retain=False)
        client.publish("blanotiger/fin",payload="Bot 3 Complete",qos=0,retain=False)
    else:
        client.publish("blanotiger/debug",payload="Error: "+str(value1),qos=0,retain=False)

def rotateL(value1):
    client.publish("blanotiger/debug",payload="Called rotateL("+str(value1)+").",qos=0,retain=False)
    gyro.rotate(-value1)
    pwm.stop()

#on_connect to the MQTT server:
def on_connect(client,userdata,flags,rc):
    print("Connection resulted in: "+connack_string(rc))
    client.subscribe("blanotiger/robot3") #subscribes upon connect
#on_disconnect to the MQTT server:    
def on_disconnect(client,userdata,rc):
    if rc!= 0:
        print("Unexpected disconnection.")
        client.reconnect()
#on_message from the MQTT server:        
def on_message(client,userdata,message):
    message.payload = message.payload.decode("utf-8")
    print("Received message "+str(message.payload)+" on topic "+message.topic+".")
    msg = str(message.payload)
    if msg=="stop":
        pwm.stop()
    elif msg=="forward":
	str8.forward(50)
    elif msg[0]=="_":
	q = int(msg[1:5])
	gyro.rotate(q)
    elif message.topic=="blanotiger/robot3":
        readIn(msg)
        print("("+str(botX)+")("+str(ballX)+")")
	findTheta()
        findMid()
        print("("+str(midpointX)+")")
	global phase
	phase=1
	driveF()
        print("Rotating...")
        rotateL(math.degrees(theta))
        print("Finished Turning.")
	phase=2
        driveF()
        print("Destination Reached.")
    else:
        client.publish("blanotiger/debug",payload="Error with Message.",qos=0,retain=False)

#This code will connect to the broker:
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect("192.168.137.124", 1883, 60) #Formatted (address, port, keepalive(seconds))

#This code will subscribe to a topic:
print("Subscribing to topic 'blanotiger/robot3'...")
client.subscribe("blanotiger/robot3",0)
print("Subscribed!")

client.loop_forever()
