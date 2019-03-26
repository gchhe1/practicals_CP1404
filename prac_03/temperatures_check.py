"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Conversion of the temperature"""
    print(MENU)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            # TODO: Write this section to convert F to C and display the result
            fahrenheit = float(input("Fahrenheit : "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
            # TODO: Write this section to convert F to C and display the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.
        else:
            print("Invalid option")
            print(MENU)
        choice = input(">>> ").upper()
    print("Thank you")


def convert_celsius_to_fahrenheit(celsius):
        """Conversion from celsius to fahrenheit"""
        celsius = celsius * 9.0 / 5 + 32
        return celsius


def convert_fahrenheit_to_celsius(fahrenheit):
        """Conversion from fahrenheit to celsius"""
        fahrenheit = 5 / 9 * (fahrenheit - 32)
        return fahrenheit


main()


