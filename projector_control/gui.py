import sys
import tkinter as tk
from tkinter import ttk, messagebox

from db import database
import commands


def ask_yes_no(var, func):
    """Messagebox function"""
    # <-- begin: Messagebox logic for power buttons
    if func == 'power_on':
        response = messagebox.askyesno(message=var)
        if response:
            commands.power_on()

    if func == 'power_off':
        response = messagebox.askyesno(message=var)
        if response:
            commands.power_off()
    # <-- end: Messagebox logic for power buttons

    # <-- begin: Messagebox logic for preset buttons
    if func == 'preset':
        last_preset = database.get('last_preset')
        if var == last_preset:
            response = messagebox.askyesno(
                message=f"Preset last set to {var},\nstill want to continue?"
            )
            if response:
                if var == 'screen':
                    commands.screen()
                else:
                    commands.backwall()
        else:
            if var == 'screen':
                commands.screen()
            else:
                commands.backwall()
    # <-- end: Messagebox logic for preset buttons


class Power(tk.Frame):
    """Power control frame and widgets"""

    def __init__(self):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        """Creates widgets in power frame"""
        power_label = tk.Label(self, text='Projector on/off')

        on_btn = ttk.Button(
            self,
            text='on',
            command=lambda: ask_yes_no('Power on projector?', 'power_on')
        )
        off_btn = ttk.Button(
            self,
            text='off',
            command=lambda: ask_yes_no('Power off projector?', 'power_off')
        )

        power_label.grid(column=0, columnspan=2, row=0, sticky=tk.NS)

        on_btn.grid(column=0, row=1)
        off_btn.grid(column=1, row=1)


class Shutter(tk.Frame):
    """Shutter frame and widgets"""

    def __init__(self):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        """Create widgets in shutter frame"""
        shutter_label = tk.Label(self, text='Shutter')

        shutter_open_btn = ttk.Button(
            self, text='open', command=commands.shutter_open)
        shutter_close_btn = ttk.Button(
            self, text='close', command=commands.shutter_close)
        shutter_freeze_btn = ttk.Button(
            self, text='freeze', command=commands.freeze)

        shutter_label.grid(column=0, columnspan=2, row=0, sticky=tk.EW)

        shutter_open_btn.grid(column=0, row=1)
        shutter_close_btn.grid(column=1, row=1)
        shutter_freeze_btn.grid(column=0, columnspan=2, row=2, sticky=tk.NS)


class LensShift(tk.Frame):
    """Lens shift frame and widgets"""

    def __init__(self):
        super().__init__()
        self.after_id = None
        self.btn_hold = False

        self.create_widgets()

    def create_widgets(self):
        """Create widgets in lens shift frame"""
        lens_shift_label = tk.Label(self, text='Manual lens shift')

        up_btn = ttk.Button(self, text='up')
        left_btn = ttk.Button(self, text='left')
        right_btn = ttk.Button(self, text='right')
        down_btn = ttk.Button(self, text='down')

        zoom_in_btn = ttk.Button(self, text='in')
        zoom_out_btn = ttk.Button(self, text='out')

        zoom_blank = tk.Frame(self, height=5)
        zoom_label = tk.Label(self, text='Zoom')

        lens_shift_label.grid(column=0, columnspan=3, row=1, sticky='N')

        up_btn.grid(column=0, columnspan=3, row=2, sticky='NS')
        left_btn.grid(column=0, row=3, sticky='E')
        right_btn.grid(column=1, row=3, sticky='W')
        down_btn.grid(column=0, columnspan=3, row=4, sticky='NS')

        zoom_blank.grid(column=0, columnspan=3, row=5, sticky='WENS')
        zoom_label.grid(column=0, columnspan=3, row=6, sticky='NS')

        zoom_in_btn.grid(column=0, row=7, sticky='E')
        zoom_out_btn.grid(column=1, row=7, sticky='W')

        up_btn.bind('<ButtonPress-1>', self.btn_down)
        up_btn.bind('<ButtonRelease-1>', self.btn_release)
        down_btn.bind('<ButtonPress-1>', self.btn_down)
        down_btn.bind('<ButtonRelease-1>', self.btn_release)

        left_btn.bind('<ButtonPress-1>', self.btn_down)
        left_btn.bind('<ButtonRelease-1>', self.btn_release)
        right_btn.bind('<ButtonPress-1>', self.btn_down)
        right_btn.bind('<ButtonRelease-1>', self.btn_release)

        zoom_in_btn.bind('<ButtonPress-1>', self.btn_down)
        zoom_in_btn.bind('<ButtonRelease-1>', self.btn_release)
        zoom_out_btn.bind('<ButtonPress-1>', self.btn_down)
        zoom_out_btn.bind('<ButtonRelease-1>', self.btn_release)

    # <-- Begin: functions controlling behavior of buttons
    def btn_down(self, event):
        """Button down behavior"""
        self.btn_hold = True
        if str(event.widget)[-1] == 'n':
            self.poll_up()
        if str(event.widget)[-1] == '2':
            self.poll_left()
        if str(event.widget)[-1] == '3':
            self.poll_right()
        if str(event.widget)[-1] == '4':
            self.poll_down()
        if str(event.widget)[-1] == '5':
            self.poll_zoom_in()
        if str(event.widget)[-1] == '6':
            self.poll_zoom_out()

    def btn_release(self, _event):
        """Release button behavior"""
        self.after_cancel(self.after_id)

    def poll_up(self):
        """Up button behavior"""
        if self.btn_hold:
            commands.vshift_inc(1)
            self.after_id = self.after(100, self.poll_up)

    def poll_down(self):
        """Down button behavior"""
        if self.btn_hold:
            commands.vshift_dec(1)
            self.after_id = self.after(100, self.poll_down)

    def poll_left(self):
        """Left button behavior"""
        if self.btn_hold:
            commands.hshift_dec(1)
            self.after_id = self.after(100, self.poll_left)

    def poll_right(self):
        """Right button behavior"""
        if self.btn_hold:
            commands.hshift_inc(1)
            self.after_id = self.after(100, self.poll_right)

    def poll_zoom_in(self):
        """Left button behavior"""
        if self.btn_hold:
            commands.zoom_dec(1)
            self.after_id = self.after(100, self.poll_zoom_in)

    def poll_zoom_out(self):
        """Right button behavior"""
        if self.btn_hold:
            commands.zoom_inc(1)
            self.after_id = self.after(100, self.poll_zoom_out)
    # <-- end: functions controlling behavior of buttons


class Preset(tk.Frame):
    """Preset frame and widgets"""

    def __init__(self):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        """Create widgets in preset frame"""
        preset_blank = tk.Frame(self, height=1)
        preset_label = tk.Label(self, text='Preset positions')

        screen_btn = ttk.Button(
            self, text='Screen',
            command=lambda: ask_yes_no('screen', 'preset')
        )
        backwall_btn = ttk.Button(
            self, text='Backwall',
            command=lambda: ask_yes_no('backwall', 'preset')
        )

        preset_blank.grid(column=0, columnspan=2, row=0, sticky='WENS')
        preset_label.grid(column=0, columnspan=2, row=1, sticky='S')

        screen_btn.grid(column=0, row=2)
        backwall_btn.grid(column=1, row=2)


class OptionsWindow(tk.Toplevel):
    """Toplevel windows for settings"""

    def __init__(self):
        super().__init__()

    def create_window(self):
        MenuBar.disabled(self)

        settings = tk.Toplevel()
        settings.title('Settings')
        settings.grab_set()
        settings.attributes('-topmost', 'true')
        settings.resizable(False, False)

        OptionsWindow.create_widgets(self, settings)

    def create_widgets(self, window):
        """Widgets for settings window"""

        zoom_steps = tk.IntVar(
            window,
            value=int(database
                      .get('options')
                      .get('steps')
                      .get('zoom'))
        )
        vert_steps = tk.IntVar(
            window,
            value=int(database
                      .get('options')
                      .get('steps')
                      .get('vertical'))
        )
        sleep_time = tk.IntVar(
            window,
            value=commands.sleep_time()
        )

        zoom_lable = tk.Label(window, text='Steps Zoom')
        zoom_entry = tk.Entry(
            window,
            width=5,
            textvariable=zoom_steps,
            justify='right'
        )
        vert_lable = tk.Label(window, text='Steps Vertical')
        vert_entry = tk.Entry(
            window,
            width=5,
            textvariable=vert_steps,
            justify='right'
        )

        spacer = ttk.Separator(window, orient='horizontal')

        sleep_lable = tk.Label(window, text='Sleep time')
        sleep_entry = tk.Entry(
            window,
            width=5,
            textvariable=sleep_time,
            justify='right'
        )

        spacer1 = ttk.Separator(window, orient='horizontal')

        ok_btn = ttk.Button(
            window,
            text='Ok',
            command=lambda: ok_command(window)
        )
        cancel_btn = ttk.Button(
            window,
            text='Cancel',
            command=lambda: destroy(window)
        )

        zoom_lable.grid(
            column=0, columnspan=3, row=0, padx=5, pady=[5, 0], sticky='w'
        )
        zoom_entry.grid(column=3, row=0, padx=5, pady=[5, 0], sticky='e')
        vert_lable.grid(column=0, row=1, padx=5, sticky='w')
        vert_entry.grid(column=3, row=1, padx=5, sticky='e')

        spacer.grid(
            column=0, columnspan=4, row=2, padx=5, pady=5, sticky='WENS'
        )

        sleep_lable.grid(column=0, row=3, padx=5, sticky='w')
        sleep_entry.grid(column=3, row=3, padx=5, sticky='e')

        spacer1.grid(
            column=0, columnspan=4, row=4, padx=5, pady=5, sticky='WENS'
        )

        ok_btn.grid(column=0, columnspan=2, padx=[5, 1], pady=[0, 5], row=5)
        cancel_btn.grid(
            column=2, columnspan=2, padx=[1, 5], pady=[0, 5], row=5
        )

        def ok_command(window):
            validated = True

            try:
                database.get('options').get('steps').update(
                    {'zoom': int(zoom_entry.get())}
                )
                database.get('options').get('steps').update(
                    {'vertical': int(vert_entry.get())}
                )
            except ValueError:
                ErrorFrame("Vertical steps and Zoom has to be a integer")
                validated = False

            if str(sleep_entry.get()) == "":
                database.get('options').get('sleeptime').update(
                    {'custom': "0"}
                )
            elif str(sleep_entry.get()) != database.get(
                    'options').get('sleeptime').get('default'):
                try:
                    database.get('options').get('sleeptime').update(
                        {'custom': float(sleep_entry.get())}
                    )
                except ValueError:
                    ErrorFrame('Sleep time has to be a floating number')
                    validated = False
            else:
                try:
                    database.get('options').get('sleeptime').pop('custom')
                except KeyError:
                    pass

            if validated:
                destroy(window)

        def destroy(window):
            MenuBar.enabled(self)
            return window.destroy()


class MenuBar(tk.Menu):
    """Pass"""

    def __init__(self):
        super().__init__()

        self.create_menu()

    def create_menu(self):
        self.file_menu = tk.Menu(self, tearoff=False)
        self.file_menu.add_command(
            label='Settings',
            underline=1,
            command=lambda: OptionsWindow.create_window(self)
        )
        self.file_menu.add_separator()
        self.file_menu.add_command(
            label='Exit',
            underline=1,
            command=sys.exit
        )
        self.add_cascade(label="File", underline=0, menu=self.file_menu)

    def disabled(self):
        self.file_menu.entryconfig('Settings', {'state': 'disabled'})

    def enabled(self):
        self.file_menu.entryconfig('Settings', {'state': 'normal'})


class ErrorFrame(tk.Frame):
    """Display error if connection to projector isn't preset"""

    def __init__(self, msg):
        super().__init__()
        self.create_widgets(msg)

    @staticmethod
    def create_widgets(msg):
        """Create widges in error frame"""
        messagebox.showerror(message=msg)


class App(tk.Tk):
    """Main program"""

    def __init__(self):
        super().__init__()
        self.title('Projector Control v1.0')
        self.resizable(False, False)

        menubar = MenuBar()
        self.config(menu=menubar)

        self.power_frame = Power()
        self.power_frame.grid(column=0, row=0, padx=5, sticky="WENS")

        self.shutter_frame = Shutter()
        self.shutter_frame.grid(column=0, row=1, padx=5, sticky='WNS')

        self.preset_frame = Preset()
        self.preset_frame.grid(column=0, row=2, padx=5,
                               pady=(0, 5), sticky='WENS')

        self.lens_shift_frame = LensShift()
        self.lens_shift_frame.grid(
            column=1, row=0, rowspan=3, padx=5, sticky='WENS')

        if not commands.check_connection():
            response = self.error_frame = ErrorFrame(
                "Can't connect to projector.")
            if response:
                self.destroy()
