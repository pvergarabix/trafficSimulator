from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_led import GroveLed
import time
import paho.mqtt.client as mqtt
import json


CounterFitConnection.init('127.0.0.1', 8000)

# semaforo interseccion 1
led0 = GroveLed(0)
led1 = GroveLed(1)
# semaforo interseccion 2
led2 = GroveLed(2)
led3 = GroveLed(3)

# conexion al broker mqtt
id = 'bcafaf37-74d1-42c3-a73f-905bd4b4b3e9'
client_name = id + 'mvp-grupo-10-Act'
client_telemetry_topic = id + '/trafficLight'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()
print("MQTT connected!")

def handle_command(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)

    if payload['led0']:
        led0.on()
    else:
        led0.off()
    if payload['led1']:
        led1.on()
    else:
        led1.off()
    if payload['led2']:
        led2.on()
    else:
        led2.off()
    if payload['led3']:
        led3.on()
    else:
        led3.off()

mqtt_client.subscribe(client_telemetry_topic)
mqtt_client.on_message = handle_command

while(True):    
    time.sleep(2)