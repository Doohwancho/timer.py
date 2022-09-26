from datetime import datetime, timedelta
import tkinter.font as tkFont
import tkinter as tk
import subprocess
from threading import *
import time 

class Clock(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config_setting();
        self.create_label()
        self.update_time()
        self.pack()
        
    def config_setting(self):
        self.master.attributes("-topmost", True)
        self.master.focus_force()
        self.master.wm_attributes("-transparent", True)
        self.master.eval('tk::PlaceWindow . center')
        self.master.title("Digital Clock")
        self.start_time = datetime.now()
        self.audio_file = "./rooster_crying.wav"

    def create_label(self):
        font_style = tkFont.Font(family="Consolas", size=60)
        self.datetime_text = tk.StringVar()
        datetime_label = tk.Label(
            self, 
            textvariable=self.datetime_text, 
            font=font_style, 
            foreground="#000000",
            background="#ffffff",
        )
        datetime_label.pack(side="top")

    def update_time(self):
        now = datetime.now()
        time_diff = now - self.start_time

        if(time_diff <= timedelta(seconds=301)):
            str_time_diff = str(time_diff).split(".")[0][2:]
            self.datetime_text.set(f"{str_time_diff}")
            self.after(1000, self.update_time)
        else:
            event = Event()
            t1 = Thread(target=sleep_handler, args= [event], daemon=True)
            t2 = Thread(target=alarm_handler, args= [self, event], daemon=True)
            
            t1.start()
            t2.start()

def sleep_handler(event):
    while(True):
        time.sleep(1)
        event.set()

def alarm_handler(self, event):
    while(True):
        event.wait()
        subprocess.call(["afplay", self.audio_file])




if __name__ == "__main__":
    root = tk.Tk()
    app = Clock(master=root)
    app.mainloop()

