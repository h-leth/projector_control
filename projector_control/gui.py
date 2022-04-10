import tkinter as tk
from tkinter import ttk

from db import read_entry
import commands

#tk.Event.
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Projector Control v1.0')
        self.geometry('205x300')
        self.resizable(False, False)
        self.btn_hold = False

        self.create_widgets()


    def btn_down(self, event):
        self.btn_hold = True
        if str(event.widget)[-1] == '5':
            self.poll_up()
        if str(event.widget)[-1] == '8':
            self.poll_down()
        if str(event.widget)[-1] == '6':
            self.poll_left()
        if str(event.widget)[-1] == '7':
            self.poll_right()

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

    
    def create_widgets(self):

        # Power on/off
        power_label = tk.Label(self, text='Projector on/off')

        on_btn = ttk.Button(self, text='on', command=commands.power_on)
        off_btn = ttk.Button(self, text='off', command=commands.power_off)

        power_label.grid(column=0, columnspan=3, row=0, sticky=tk.NS)

        on_btn.grid(column=0, row=1)
        off_btn.grid(column=1, columnspan=2, row=1)
        
        # Shutter open/close
        
        shutter_label = tk.Label(self, text='Shutter open/close')

        shutter_open_btn = ttk.Button(self, text='open')
        shutter_close_btn = ttk.Button(self, text='close')
        
        shutter_label.grid(column=0, columnspan=3, row=2, sticky=tk.NS)

        shutter_open_btn.grid(column=0, row=3)
        shutter_close_btn.grid(column=1, columnspan=2, row=3)

        # Manual lens shift
        lens_shift_blank = tk.Frame(self, height=1, bg='lightgray')
        lens_shift_label = tk.Label(self, text='Manual lens shift')

        up_btn = ttk.Button(self, text='up')
        zoom_in_btn = ttk.Button(self, text='in')
        zoom_out_btn = ttk.Button(self, text='out')
        down_btn = ttk.Button(self, text='down')

        lens_shift_blank.grid(column=0, columnspan=3, row=4, pady=7, padx=7, sticky='WENS')
        lens_shift_label.grid(column=0, columnspan=3, row=5, sticky='NS')

        up_btn.grid(column=0, columnspan=3, row=6, sticky='NS')
        zoom_in_btn.grid(column=0, row=7, sticky='E')
        zoom_out_btn.grid(column=1, row=7, sticky='W')
        down_btn.grid(column=0, columnspan=3, row=8, sticky='NS')

        up_btn.bind('<ButtonPress-1>', self.btn_down)
        up_btn.bind('<ButtonRelease-1>', self.btn_relase)

        down_btn.bind('<ButtonPress-1>', self.btn_down)
        down_btn.bind('<ButtonRelease-1>', self.btn_relase)

        # Presets
        preset_blank = tk.Frame(self, height=1, bg='lightgrey')
        preset_label = tk.Label(self, text='Preset positions')

        screen_btn = ttk.Button(self, text='Screen', command=commands.screen)
        backwall_btn = ttk.Button(self, text='Backwall', command=commands.backwall)

        preset_blank.grid(column=0, columnspan=3, row=9, pady=7, padx=7, sticky='WENS')
        preset_label.grid(column=0, columnspan=3, row=10, sticky='S')

        screen_btn.grid(column=0, row=11)
        backwall_btn.grid(column=1, row=11)


if __name__ == '__main__':
    app = App()
    app.mainloop()

