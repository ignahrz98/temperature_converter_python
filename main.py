import tkinter as tk
from tkinter import ttk
import converter as con

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
        print("From Celsius to Fahrenheit")
        degrees_converted = con.celcius_to_fahrenheit(degrees)
        print(degrees_converted)
        label_result.config(text=f"Resultado: {degrees_converted} °F")
    elif convert_from == 1 and convert_to == 0:
        print("From Fahrenheit to Celsius")
        degrees_converted = con.fahrenheit_to_celcius(degrees)
        print(degrees_converted)
        label_result.config(text=f"Resultado: {degrees_converted} °C")



window = tk.Tk()
window.title("Temperature converter")
window.geometry("400x300")
window.resizable(False, False)

label_for_input_degrees = tk.Label(window, text="Ingrese grados a convertir", font=("Arial", 12))
label_for_input_degrees.pack(padx=10, pady=10)

input_degrees = tk.Entry(window, width=8, font=("Arial", 12))
input_degrees.pack()

frame_selection = tk.Frame(window, padx=10, pady=10)
frame_selection.pack()

combobox_convert_from = ttk.Combobox(frame_selection, state="readonly")
combobox_convert_from.pack(side="left", padx=5)

elements_combobox_convert_from = ["Convertir de Celcius (°C)", "Convertir de Fahrenheit (°F)"]
combobox_convert_from["values"] = elements_combobox_convert_from

combobox_convert_to = ttk.Combobox(frame_selection, state="readonly")
combobox_convert_to.pack(side="left", padx=5)

elements_combobox_convert_to = ["Convertir a Celcius (°C)", "Convertir a Fahrenheit (°F)"]
combobox_convert_to["values"] = elements_combobox_convert_to

button = tk.Button(window, text="Convertir")
button.pack()
button.config(command=converter)

label_result = tk.Label(text="", font=("Arial", 12), pady=10)
label_result.pack()

window.mainloop()