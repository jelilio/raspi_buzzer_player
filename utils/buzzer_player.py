import RPi.GPIO as GPIO
import time
from utils.buzzer_source import available_tones


class BuzzerPlayer(object):

    def __init__(self, buzzer_pin):
        self.buzzer_pin = buzzer_pin

    def setup(self):
        # GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location BOARD
        GPIO.setup(self.buzzer_pin, GPIO.OUT)

    def play(self, buzzer_type):
        config = available_tones[buzzer_type]
        (melody, tempo, pause, pace) = config
        self.__play(melody, tempo, pause, pace)

    def __play(self, melody, tempo, pause, pace=0.800):
        for i in range(0, len(melody)):  # Play song
            noteDuration = pace / tempo[i]
            self.__buzz(melody[i], noteDuration)  # Change the frequency along the song note
            pauseBetweenNotes = noteDuration * pause
            time.sleep(pauseBetweenNotes)

    def __buzz(self, frequency, length):  # create the function "buzz" and feed it the pitch and duration)
        if frequency == 0:
            time.sleep(length)
            return

        period = 1.0 / frequency  # in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
        delayValue = period / 2  # calculate the time for half of the wave
        numCycles = int(length * frequency)  # the number of waves to produce is the duration times the frequency

        for i in range(numCycles):  # start a loop from 0 to the variable "cycles" calculated above
            GPIO.output(self.buzzer_pin, True)  # set pin 27 to high
            time.sleep(delayValue)  # wait with pin 27 high
            GPIO.output(self.buzzer_pin, False)  # set pin 27 to low
            time.sleep(delayValue)  # wait with pin 27 low
