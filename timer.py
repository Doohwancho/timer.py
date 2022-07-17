from datetime import datetime
import tkinter.font as tkFont
import tkinter as tk


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
        time_diff = str(now - self.start_time).split(".")[0]
        text = f"{time_diff}"
        self.datetime_text.set(text)
        self.after(1000, self.update_time)


if __name__ == "__main__":
    root = tk.Tk()
    app = Clock(master=root)
    app.mainloop()
