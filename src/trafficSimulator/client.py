import paho.mqtt.client as mqtt
import json

class Client:
    def __init__(self):
        self.id = 'bcafaf37-74d1-42c3-a73f-905bd4b4b3e9'
        self.client_name = self.id + 'mvp-grupo-10'
        self.client_telemetry_topic = self.id + '/trafficLight'
        self.mqtt_client = None
        self.estado1 = True
        self.estado2 = False
        print("Objeto Client Inicializado")
        self.conect()

    def conect(self):
        # create an MQTT client object and connect to the MQTT broker
        mqtt_client = mqtt.Client(self.client_name)
        mqtt_client.connect('test.mosquitto.org')
        mqtt_client.loop_start()        
        self.mqtt_client = mqtt_client
        print("MQTT connected!")

    def upd_send_info(self):
        #para enviar los comandos ---> 
        self.estado1 = not self.estado1
        self.estado2 = not self.estado2

        print(f"nuevo estado1: {self.estado1}")
        print(f"nuevo estado2: {self.estado2}")

        trafficLight = json.dumps(
        {
        'led0':self.estado1,
        'led1':self.estado2,
        'led2':self.estado2,
        'led3':self.estado1
        })
        self.mqtt_client.publish(self.client_telemetry_topic, trafficLight)
        print("se ejecuto upd_send_info!")









