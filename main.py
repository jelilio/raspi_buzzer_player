import time

import RPi.GPIO as GPIO

from pir_sensor import PirSensor
from utils.buzzer_player import BuzzerPlayer
from utils.buzzer_type import BuzzerType

buzzer_player = BuzzerPlayer(buzzer_pin=11)
pir_sensor = PirSensor(pir_sensor_pin=7)


def destroy():
    GPIO.cleanup()


def run(pirPin):
    print('motion detected')
    buzzer_player.play(buzzer_type=BuzzerType.TWINKLE_TWINKLE)
    time.sleep(10)


if __name__ == "__main__":
    try:
        buzzer_player.setup()
        pir_sensor.setup()
        pir_sensor.activate(run)
        while True:
            pass
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
