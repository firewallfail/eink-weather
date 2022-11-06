import requests

from tkinter import *
from tkinter import ttk


def update(*args):
    try:
        current_weather.set("current weather")
    except ValueError:
        pass


root = Tk()
root.title("Weather")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

button = ttk.Button(root, text="Get Weather", command="update")
button.grid()


current_weather = StringVar()
current_weather_label = ttk.Label(root, textvariable=current_weather)
current_weather_label.grid()

root.bind("<Return>", update)

root.geometry("800x480")
# root.overrideredirect(True)

root.mainloop()
