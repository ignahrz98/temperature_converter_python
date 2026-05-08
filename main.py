import tkinter as tk
from tkinter import ttk
import converter as con
import definitions as toplevel_def

def converter():
    try:
        degrees = int(input_degrees.get())
        print(f"Degrees: {degrees}")
    except:
        print("Degrees is empty")
        label_result.config(text="")

    convert_from = combobox_convert_from.current()
    convert_to = combobox_convert_to.current()
    print(f"{convert_from} a {convert_to}")

    if convert_from == 0 and convert_to == 1:
        degrees_converted = con.celsius_to_fahrenheit(degrees)
        print(degrees_converted)
        label_result.config(text=f"Result: {degrees_converted} °F")
    elif convert_from == 0 and convert_to == 2:
        degrees_converted = con.celsius_to_kelvin(degrees)
        label_result.config(text=f"Result: {degrees_converted} K")
    elif convert_from == 1 and convert_to == 0:
        degrees_converted = con.fahrenheit_to_celsius(degrees)
        print(degrees_converted)
        label_result.config(text=f"Result: {degrees_converted} °C")
    elif convert_from == 1 and convert_to == 2:
        degrees_converted = con.fahrenheit_to_kelvin(degrees)
        label_result.config(text=f"Result: {degrees_converted} K")
    elif convert_from == 2 and convert_to == 0:
        degrees_converted = con.kelvin_to_celsius(degrees)
        label_result.config(text=f"Result: {degrees_converted} °C")
    elif convert_from == 2 and convert_to == 1:
        degrees_converted = con.kelvin_to_fahrenheit(degrees)
        label_result.config(text=f"Result: {degrees_converted} °F")



window = tk.Tk()
window.title("Temperature converter")
window.geometry("400x300")
window.resizable(False, False)

top_menu = tk.Menu(window)
window.config(menu=top_menu)

info_menu = tk.Menu(top_menu, tearoff=0)
top_menu.add_cascade(label="Info", menu=info_menu)
info_menu.add_command(label="Definitions", command=lambda: toplevel_def.toplevel_definitions(window))

label_for_input_degrees = tk.Label(window, text="Write degrees", font=("Arial", 12))
label_for_input_degrees.pack(padx=10, pady=10)

input_degrees = tk.Entry(window, width=8, font=("Arial", 12))
input_degrees.pack()

frame_selection = tk.Frame(window, padx=10, pady=10)
frame_selection.pack()

combobox_convert_from = ttk.Combobox(frame_selection, state="readonly")
combobox_convert_from.pack(side="left", padx=5)

elements_combobox_convert_from = ["Convert from Celsius (°C)", "Convert from Fahrenheit (°F)", "Convert from Kelvin (K)"]
combobox_convert_from["values"] = elements_combobox_convert_from

combobox_convert_to = ttk.Combobox(frame_selection, state="readonly")
combobox_convert_to.pack(side="left", padx=5)

elements_combobox_convert_to = ["Convert to Celsius (°C)", "Convert to Fahrenheit (°F)", "Convert to Kelvin (K)"]
combobox_convert_to["values"] = elements_combobox_convert_to

button = tk.Button(window, text="Convert")
button.pack()
button.config(command=converter)

label_result = tk.Label(text="", font=("Arial", 12), pady=10)
label_result.pack()

window.mainloop()