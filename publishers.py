import paho.mqtt.client as mqttClient
import threading
from time import sleep
from sys import argv

def publisher(index):
    threadName = "Publisher " + index
    client = mqttClient.Client(threadName)

    client.connect("127.0.0.1", 1883, 60)

    while 1:
        client.publish("Testing", "message")
        sleep(int(intervaloEnvioMsg))

numPublishers = int(argv[1])
intervaloEnvioMsg = float(argv[2])

for i in range(0, numPublishers):
    thread = threading.Thread(target=publisher, args=(str(i),)).start()