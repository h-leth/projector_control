import tkinter as tk
from tkinter import ttk

from db import read_entry
import commands


class Power(tk.Frame):
    """Power control frame and widgets"""

    def __init__(self):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        power_label = tk.Label(self, text='Projector on/off')

        on_btn = ttk.Button(self, text='on', command=commands.power_on)
        off_btn = ttk.Button(self, text='off', command=commands.power_off)

        power_label.grid(column=0, columnspan=2, row=0, sticky=tk.NS)

        on_btn.grid(column=0, row=1)
        off_btn.grid(column=1, row=1)


class Shutter(tk.Frame):
    """Shutter frame and widgets"""

    def __init__(self):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        shutter_label = tk.Label(self, text='Shutter open/close')

        shutter_open_btn = ttk.Button(
            self, text='open', command=commands.shutter_open)
        shutter_close_btn = ttk.Button(
            self, text='close', command=commands.shutter_close)

        shutter_label.grid(column=0, columnspan=2, row=0, sticky=tk.NS)

        shutter_open_btn.grid(column=0, row=1)
        shutter_close_btn.grid(column=1, row=1)


class Lens_shift(tk.Frame):
    """Lens shift frame and widgets"""

    def __init__(self):
        super().__init__()
        self.btn_hold = False

        self.create_widgets()

    def create_widgets(self):
        lens_shift_blank = tk.Frame(self, height=1, bg='lightgray')
        lens_shift_label = tk.Label(self, text='Manual lens shift')

        up_btn = ttk.Button(self, text='up')
        zoom_in_btn = ttk.Button(self, text='in')
        zoom_out_btn = ttk.Button(self, text='out')
        down_btn = ttk.Button(self, text='down')

        lens_shift_blank.grid(column=0, columnspan=3, row=0, sticky='WENS')
        lens_shift_label.grid(column=0, columnspan=3, row=1, sticky='NS')

        up_btn.grid(column=0, columnspan=3, row=2, sticky='NS')
        zoom_in_btn.grid(column=0, row=3, sticky='E')
        zoom_out_btn.grid(column=1, row=3, sticky='W')
        down_btn.grid(column=0, columnspan=3, row=4, sticky='NS')

        up_btn.bind('<ButtonPress-1>', self.btn_down)
        up_btn.bind('<ButtonRelease-1>', self.btn_relase)
        down_btn.bind('<ButtonPress-1>', self.btn_down)
        down_btn.bind('<ButtonRelease-1>', self.btn_relase)

        zoom_in_btn.bind('<ButtonPress-1>', self.btn_down)
        zoom_in_btn.bind('<ButtonRelease-1>', self.btn_relase)
        zoom_out_btn.bind('<ButtonPress-1>', self.btn_down)
        zoom_out_btn.bind('<ButtonRelease-1>', self.btn_relase)

    # <-- Begin: functions controlling behavior of buttons
    def btn_down(self, event):
        self.btn_hold = True
        if str(event.widget)[-1] == 'n':
            self.poll_up()
        if str(event.widget)[-1] == '2':
            self.poll_left()
        if str(event.widget)[-1] == '3':
            self.poll_right()
        if str(event.widget)[-1] == '4':
            self.poll_down()

    def btn_relase(self, event):
        self.after_cancel(self.after_id)

    def poll_up(self):
        if self.btn_hold:
            commands.vshift_inc(1)
            self.after_id = self.after(100, self.poll_up)

    def poll_down(self):
        if self.btn_hold:
            commands.vshift_dec(1)
            self.after_id = self.after(100, self.poll_down)

    def poll_left(self):
        if self.btn_hold:
            commands.zoom_inc(1)
            self.after_id = self.after(100, self.poll_left)

    def poll_right(self):
        if self.btn_hold:
            commands.zoom_dec(1)
            self.after_id = self.after(100, self.poll_right)
    # <-- end: functions controlling behavior of buttons


class Preset(tk.Frame):
    """Preset frame and widgets"""

    def __init__(self):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        preset_blank = tk.Frame(self, height=1, bg='lightgrey')
        preset_label = tk.Label(self, text='Preset positions')

        screen_btn = ttk.Button(
            self, text='Screen', command=commands.screen
        )
        backwall_btn = ttk.Button(
            self, text='Backwall', command=commands.backwall
        )

        preset_blank.grid(column=0, columnspan=2, row=0, sticky='WENS')
        preset_label.grid(column=0, columnspan=2, row=1, sticky='S')

        screen_btn.grid(column=0, row=2)
        backwall_btn.grid(column=1, row=2)


class App(tk.Tk):
    """Main program"""

    def __init__(self):
        super().__init__()
        self.title('Projector Control v1.0')
        self.resizable(False, False)

        self.power_frame = Power()
        self.power_frame.grid(column=0, row=0, padx=5, sticky="WENS")

        self.shutter_frame = Shutter()
        self.shutter_frame.grid(column=0, row=1, padx=5, sticky='WENS')

        self.lens_shift_frame = Lens_shift()
        self.lens_shift_frame.grid(
            column=0, row=2, padx=5, pady=5, sticky='WENS')

        self.preset_frame = Preset()
        self.preset_frame.grid(column=0, row=3, padx=5,
                               pady=(0, 5), sticky='WENS')


if __name__ == '__main__':
    app = App()
    app.mainloop()
