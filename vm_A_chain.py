import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe("adhishch/pong")
    client.publish("adhishch/ping", "1")
    client.message_callback_add("adhishch/ping", on_message_ping)

def on_message_ping(client, userdata, msg):
    number = int(msg.payload.decode()) + 1
    print(f"Received: {msg.payload.decode()}, Sending: {number}")
    time.sleep(1)
    client.publish("adhishch/ping", str(number))

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect("172.20.10.3", 1883, 60)
    client.loop_forever()
    #time.sleep(2)