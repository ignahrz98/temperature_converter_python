import tkinter as tk

def toplevel_definitions(window_parent):
    window_definitions = tk.Toplevel(window_parent)
    window_definitions.title("Definitions")
    window_definitions.geometry("300x200")
    window_definitions.grab_set()

    content_definitions = tk.Text(window_definitions, wrap="word")
    content_definitions.insert("1.0", """Celsius (°C)
A scale for measuring temperature in which 0° is the freezing point of water and 100° is the boiling point, under standard atmospheric pressure. It is the primary temperature scale used in most countries and for scientific purposes worldwide.
----
Fahrenheit (°F)
A temperature scale where the freezing point of water is 32° and the boiling point is 212°. These two points are exactly 180 degrees apart. This scale is primarily used for weather and everyday life in the United States and a few other territories.""")
    content_definitions.config(state="disabled")
    content_definitions.pack()