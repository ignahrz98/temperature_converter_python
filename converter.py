def celcius_to_fahrenheit(degrees):
    return round((degrees * (9/5)) + 32, 1)

def celsius_to_kelvin(degrees):
    return round((degrees + 273.15), 2)

def fahrenheit_to_celcius(degrees):
    return round((degrees - 32) * (5/9), 1)

def fahrenheit_to_kelvin(degrees):
    celsius = fahrenheit_to_celcius(degrees)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(degrees):
    return round((degrees - 273.15), 1)

def kelvin_to_fahrenheit(degrees):
    celsius = kelvin_to_celsius(degrees)
    return celcius_to_fahrenheit(celsius)