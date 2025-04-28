# Librerías necesarias
import network
import machine
from umqtt.simple import MQTTClient
from machine import Pin
from time import sleep

# Configuración de red WiFi
WIFI_SSID = "INFINITUM0593"
WIFI_PASSWORD = "XhSN23Gn2h"

# Configuración MQTT
MQTT_BROKER = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "R2"

# Función para conectar al WiFi
def conectar_wifi():
    print("Conectando a WiFi...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.5)
    print("\nWiFi conectada!")

# Función que se ejecuta al recibir un mensaje MQTT
def llegada_mensaje(topic, msg):
    print("Mensaje recibido:", msg)
    if msg == b'ON':
        led.value(1)  # Encender LED
    elif msg == b'OFF':
        led.value(0)  # Apagar LED

# Función para suscribirse al broker MQTT
def subscribir_mqtt():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)
    client.set_callback(llegada_mensaje)
    client.connect()
    client.subscribe(MQTT_TOPIC)
    print("Conectado a broker:", MQTT_BROKER)
    print("Suscrito al tópico:", MQTT_TOPIC)
    return client

# Declaración del pin para el LED
led = Pin(13, Pin.OUT)  # LED en el pin GPIO2
led.value(0)  # LED apagado al iniciar

# Conexión a WiFi
conectar_wifi()

# Conexión y suscripción a MQTT
client = subscribir_mqtt()

# Bucle principal
while True:
    client.wait_msg()
