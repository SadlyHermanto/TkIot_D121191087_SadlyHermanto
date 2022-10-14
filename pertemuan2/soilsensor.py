from pymata4 import pymata4
import time
board = pymata4.Pymata4()

port = "COM5"

analog_pin = 0
digital_pin = 8

board.set_pin_mode_analog_input(analog_pin)
board.set_pin_mode_digital_input(digital_pin)

while True:
    value = board.analog_read(analog_pin)
    print(value)
    time.sleep(1)
