"""
Extension, Convert Temps
"""


def main():
    fahrenheit = get_input_from_file()
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    output_temperature(celsius)


def get_input_from_file():
    temperature_fahrenheit = []
    temperature_input = open("temps_input.txt", "r")
    for temperature in temperature_input:
        temperature_fahrenheit.append(float(temperature))
    temperature_input.close()
    return temperature_fahrenheit


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = []
    for temperature in fahrenheit:
        converted_celsius = 5 / 9 * (temperature - 32)
        celsius.append(converted_celsius)
    return celsius


def output_temperature(celsius):
    temperature_output = open("temps_output.txt", "w")
    for temperature in celsius:
        print(temperature, file=temperature_output)
    temperature_output.close()


main()
