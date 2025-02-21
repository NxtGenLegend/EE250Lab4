import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.publish("adhishch/ping", "1")

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect("172.20.10.3", 1883, 60)
    client.loop_start()
    time.sleep(2)