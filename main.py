import tkinter as tk
from tkinter import ttk

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

combobox_convert_from = ttk.Combobox(frame_selection)
combobox_convert_from.pack(side="left", padx=5)

elements_combobox_convert_from = ["Convertir de Celcius (°C)", "Convertir de Fahrenheit (°F)"]
combobox_convert_from["values"] = elements_combobox_convert_from

combobox_convert_to = ttk.Combobox(frame_selection)
combobox_convert_to.pack(side="left", padx=5)

elements_combobox_convert_to = ["Convertir a Celcius (°C)", "Convertir a Fahrenheit (°F)"]
combobox_convert_to["values"] = elements_combobox_convert_to

button = tk.Button(window, text="Convertir")
button.pack()

window.mainloop()