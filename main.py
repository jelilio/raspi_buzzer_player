import RPi.GPIO as GPIO
from utils.buzzer_player import BuzzerPlayer


def destroy():
    GPIO.cleanup()


if __name__ == "__main__":
    try:
        buzzer_player = BuzzerPlayer(11)
        buzzer_player.setup()
        destroy()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
