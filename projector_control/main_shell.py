import sys
import user_interface as ui
from db import read_entry
from commands import screen, backwall


if __name__ == '__main__':
    main_loop = True

    while True:
        try:
            ui.main_screen()
            entry = read_entry()
            command = input('Select: ')

            if command == '1':
                if entry != 'backwall':
                    backwall()
                else:
                    if ui.confirm('backwall'):
                        backwall()

            elif command == '2':
                if entry != 'screen':
                    screen()
                else:
                    if ui.confirm('screen'):
                        screen()

            elif command == '3':
                ui.manual_shift_zoom()
            elif command.lower() == 'q':
                sys.exit()

            else:
                print('\nInvalid input, try again')
                input('Press key to continue')
        except KeyboardInterrupt:
            break
