import uasyncio as asyncio
from machine import Pin

# Configuración de pines
led_pin = Pin(2, Pin.OUT)  # Pin de salida para el LED
button_pin = Pin(0, Pin.IN, Pin.PULL_UP)  # Pin de entrada para el botón

async def blink_led():
    while True:
        led_pin.value(not led_pin.value())
        await asyncio.sleep(0.5)  # Parpadeo cada 500ms

async def monitor_button():
    while True:
        if button_pin.value() == 0:  # Botón presionado
            led_pin.value(1)  # Encender LED
        else:
            led_pin.value(0)  # Apagar LED
        await asyncio.sleep(0.1)  # Verificar el estado del botón cada 100ms

async def main():
    task1 = asyncio.create_task(blink_led())
    task2 = asyncio.create_task(monitor_button())
    await asyncio.gather(task1, task2)

asyncio.run(main())