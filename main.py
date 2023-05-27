import RPi.GPIO as GPIO
from utils.buzzer_player import BuzzerPlayer
from utils.buzzer_type import BuzzerType


def destroy():
    GPIO.cleanup()


if __name__ == "__main__":
    try:
        buzzer_player = BuzzerPlayer(buzzer_pin=11)
        buzzer_player.setup()
        buzzer_player.play(buzzer_type=BuzzerType.UNDERWORLD)
        destroy()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
