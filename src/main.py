import random
import sys

from gpio import dance, led_control, servo_control
from music import music_player, speech_input

controller = servo_control.ServoController()
led = led_control.LEDController()
dance_queue = {}


def callback(data):
    print(data)
    dance_queue.execute_move(data)


def execute(command):
    global dance_queue
    if command != None:
        print(command)
        if command[0] == "play":
            dance_queue = dance.DanceQueue(10000, controller, led)
            music_player.play_from_search(command[1], callback)
        elif command[0] == "stop":
            music_player.stop()
        elif command[0] == "led":
            print(command)
            if len(command) == 2:
                led.set_r(float(command[1]))
                led.set_g(float(command[1]))
                led.set_b(float(command[1]))
        elif command[0] == "servo":
            print(command)
            if len(command) == 2:
                controller.move_arm_l(float(command[1]))
                controller.move_arm_r(float(command[1]))
                controller.move_head(float(command[1]))
                controller.move_body(float(command[1]))
        elif command[0] == "cleanup":
            controller.cleanup()
            sys.exit(0)


while 1:
    # speech_input.start(play)
    c = input().split()
    a = (c[0], " ".join(c[1:]))
    execute(a)
