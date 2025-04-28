import machine
import time
import dht

# Configuración de pines
dht_pin = machine.Pin(27)  # Pin donde está conectado el DHT11 (ejemplo: GPIO4)
led_pin = machine.Pin(14, machine.Pin.OUT)  # Pin donde está la LED (ejemplo: GPIO2)

# Inicializar el sensor DHT11
sensor = dht.DHT11(dht_pin)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()  # Leer temperatura en °C

        print("Temperatura:", temp, "°C")

        if temp >= 30:
            led_pin.on()   # Encender LED
        else:
            led_pin.off()  # Apagar LED

    except OSError as e:
        print('Fallo al leer el sensor.')

    time.sleep(2)  # Esperar 2 segundos
