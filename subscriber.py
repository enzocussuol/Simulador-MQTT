import paho.mqtt.client as mqttClient
import threading
from sys import argv

def subscriber(index):
    threadName = "Subscriber " + index

    client = mqttClient.Client(threadName)
    client.subscribe("Testing")

    client.connect("127.0.0.1", 1883, 60)

    while 1:
        client.loop()

numSubscribers = int(argv[1])

for i in range(0, numSubscribers):
    thread = threading.Thread(target=subscriber, args=(str(i),)).start()