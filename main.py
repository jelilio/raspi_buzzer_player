import time
import RPi.GPIO as GPIO
from gpiozero import MotionSensor


# from pir_sensor import PirSensor
from utils.buzzer_player import BuzzerPlayer
from utils.buzzer_type import BuzzerType

buzzer_player = BuzzerPlayer(buzzer_pin=17)
# pir_sensor = PirSensor(pir_sensor_pin=7)
pir = MotionSensor(4)


def destroy():
    GPIO.cleanup()


def run(pirPin):
    print('motion detected')
    buzzer_player.play(buzzer_type=BuzzerType.TWINKLE_TWINKLE)
    time.sleep(10)


if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BCM)
        buzzer_player.setup()
        buzzer_player.play(buzzer_type=BuzzerType.TWINKLE_TWINKLE)
        # pir_sensor.setup()
        # pir_sensor.activate(run)
        while True:
            print("Waiting for motion")
            pir.wait_for_motion()
            print("You moved")
            buzzer_player.play(buzzer_type=BuzzerType.TWINKLE_TWINKLE)
            print("about to sleep")
            time.sleep(10)
            print("wake up from sleep")
            pir.wait_for_no_motion()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
