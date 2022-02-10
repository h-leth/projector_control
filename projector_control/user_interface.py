import os
from pynput import keyboard

from commands import *


def clear():
    if os.system == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main_screen():
    clear()
    print('''
Main menu

1 - Move to backwall
2 - Move to screen
3 - Manual shift/zoom

q - Quit progam
    ''')


def manual_shift_zoom():
    clear()
    print('''
Manual lens shift/zoom
(use arrow keys to controll)

up - Shift lens up
down - Shift lens down
left - Zoom in
right - Zoom out

esc - Return to main menu
            ''')

    def on_press(key):
        if key == keyboard.Key.up:
            print(vshift_inc(1))
        if key == keyboard.Key.down:
            print(vshift_dec(1))
        if key == keyboard.Key.left:
            print(zoom_inc(1))
        if key == keyboard.Key.right:
            print(zoom_dec(1))

    def on_release(key):
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release,
            suppress=True) as listener:
        listener.join()


def confirm(x):
    while True:
        main_screen()
        allowed_input = {'y', 'n'}

        print(f'\nProjector was last set to {x},')
        prompt = input('still want to do it? (y/n): ').lower()
        if prompt not in allowed_input:
            print('\nInvalid input, try again')
            input('Press key to continue')
        else:
            if prompt.lower() == 'y':
                return True
            else:
                return False
