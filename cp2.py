#!/usr/bin/env python3

# Cordwood Puzzle (second edition) by Boldport
# Boldport Club project #3, May 2016
# This program controls the Boldport Cordwood Puzzle (v2) using the 2N7000 n-channel FETs on the board.
# Made by Dries Renmans, 20160516 (mailto:dries.renmans@telenet.be)

# Dependencies: python3, RPi.GPIO
import RPi.GPIO as GPIO
from time import sleep
from random import randint

# List for the LEDs on the board (2 red, 2 yellow, 2 green).
# If you want to use other GPIO pins, only this list needs to be changed.
# See info for connections.
led_list = [13, 21, 19, 20, 26, 16]

GPIO.setmode(GPIO.BCM)
# Setup for LEDs
GPIO.setup(led_list, GPIO.OUT, initial=GPIO.LOW)

def main():
    # print('You are using this program at your own risk.')
    # input('Press enter if you want to continue.')
    while True:
        print()
        print('Main menu:', '\n')
        print('1 - Random mode')
        print('2 - Traffic light mode')
        print('3 - LED chase mode')
        print('4 - Blink mode')
        print('5 - Arrows mode')
        print('6 - Jumpy LED mode', '\n')
        print('I - Info')
        print('Q - Quit', '\n')
        print('Note - Press Ctrl+C while looping to come back to this menu!', '\n')
        mode_select = input('Enter mode: ')
        if mode_select not in ('1', '2', '3', '4', '5', '6', 'i', 'I', 'q', 'Q'):
            print('\n', '--- Not an option! ---', '\n')
            continue
        if mode_select == '1':
            print('Random mode')
            state = (0, 0, 0, 0, 0, 0)
            try:
                while True:
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1))
            except KeyboardInterrupt:
                pass
        elif mode_select == '2':
            print('Traffic light mode')
            try:
                while True:
                    state = (0, 0, 0, 0, 1, 1)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(5)
                    state = (0, 0, 1, 1, 0, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(1)
                    state = (1, 1, 0, 0, 0, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(5)
            except KeyboardInterrupt:
                pass
        elif mode_select == '3':
            print('Circular mode')
            try:
                while True:
                    state = (0, 0, 0, 0, 0, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (1, 0, 0, 0, 0, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (1, 1, 0, 0, 0, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (1, 1, 1, 0, 0, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (1, 1, 1, 1, 0, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (1, 1, 1, 1, 1, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (1, 1, 1, 1, 1, 1)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (0, 1, 1, 1, 1, 1)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (0, 0, 1, 1, 1, 1)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (0, 0, 0, 1, 1, 1)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (0, 0, 0, 0, 1, 1)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (0, 0, 0, 0, 0, 1)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
            except KeyboardInterrupt:
                pass
        elif mode_select == '4':
            print('Blink mode')
            try:
                while True:
                    state = (0, 0, 0, 0, 0, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(1)
                    state = (1, 1, 1, 1, 1, 1)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(1)
            except KeyboardInterrupt:
                pass
        elif mode_select == '5':
            print('Arrows mode')
            try:
                while True:
                    state = (1, 0, 0, 1, 1, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(1)
                    state = (0, 1, 1, 0, 0, 1)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(1)
            except KeyboardInterrupt:
                pass
        elif mode_select == '6':
            print('Jumpy LED mode')
            try:
                while True:
                    state = (1, 0, 0, 0, 0, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (0, 1, 0, 0, 0, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (0, 0, 1, 0, 0, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (0, 0, 0, 1, 0, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (0, 0, 0, 0, 1, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (0, 0, 0, 0, 0, 1)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (0, 0, 0, 0, 1, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (0, 0, 0, 1, 0, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (0, 0, 1, 0, 0, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
                    state = (0, 1, 0, 0, 0, 0)
                    print('State: {0}'.format(state))
                    GPIO.output(led_list, state)
                    sleep(0.5)
            except KeyboardInterrupt:
                pass
        elif mode_select == 'I' or mode_select == 'i':
            print()
            print('Connect the pins of the Cordwood board to following GPIO pins on the Raspberry Pi:', '\n')
            print('Red LED 1 (pin 1): GPIO 13')
            print('Red LED 2 (pin 4): GPIO 16')
            print('Yellow LED 1 (pin 2): GPIO 19')
            print('Yellow LED 2 (pin 5): GPIO 20')
            print('Green LED 1 (pin 3): GPIO 26')
            print('Green LED 2 (pin 6): GPIO 21', '\n')
            print('Connect the ground pin on the opposite side of the Cordwood board to any ground on the Raspberry Pi.')
            print('Connect the power to a 3.3V pin on the Raspberry Pi.')
            print('WARNING: POWERING THE BOARD WITH 5V MIGHT DAMAGE YOUR RPI GPIOs AS THE FETs ON THE BOARD ARE PULLED UP TO THE SAME VOLTAGE!')
            print('RASPBERRY PI GPIOs ARE 3.3V!!')
            print()
            input('Press enter to continue.')
            pass
        elif mode_select == 'Q' or mode_select == 'q':
            print()
            print('Goodbye!')
            break
    GPIO.cleanup()
    print('GPIOs cleaned!')

if __name__ == '__main__':
    main()
