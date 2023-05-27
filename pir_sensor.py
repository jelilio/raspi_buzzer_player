import RPi.GPIO as GPIO


class PirSensor(object):

    def __init__(self, pir_sensor_pin):
        self.pir_sensor_pin = pir_sensor_pin

    def setup(self):
        GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
        GPIO.setup(self.pir_sensor_pin, GPIO.IN)

    def activate(self, callback):
        # adding a callback function when the pir sensor output rises when motion is detected
        GPIO.add_event_detect(self.pir_sensor_pin, GPIO.RISING, callback=callback)