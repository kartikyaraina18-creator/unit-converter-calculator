

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kg_to_pound(kg):
    return kg * 2.20462

def pound_to_kg(pound):
    return pound / 2.20462

# --- Main Program ---

def unit_converter():
    print("=========================================")
    print("    WELCOME TO UNIT CONVERTER CALCULATOR ")
    print("=========================================")

    # Loop to keep the calculator running until the user exits (Feature 8)
    while True:
        print("\nPlease choose a conversion option:")
        print("1. KM to Miles")
        print("2. Miles to KM")
        print("3. Celsius to Fahrenheit")
        print("4. Fahrenheit to Celsius")
        print("5. KG to Pound")
        print("6. Pound to KG")
        print("7. Exit")

        # User Input (Feature 7)
        choice = input("\nEnter your choice (1-7): ")

        if choice == '7':
            print("Thank you for using the Unit Converter. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                value = float(input("Enter the value to convert: "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

            if choice == '1':
                result = km_to_miles(value)
                print(f"{value} KM = {result:.2f} Miles")

            elif choice == '2':
                result = miles_to_km(value)
                print(f"{value} Miles = {result:.2f} KM")

            elif choice == '3':
                result = celsius_to_fahrenheit(value)
                print(f"{value}°C = {result:.2f}°F")

            elif choice == '4':
                result = fahrenheit_to_celsius(value)
                print(f"{value}°F = {result:.2f}°C")

            elif choice == '5':
                result = kg_to_pound(value)
                print(f"{value} KG = {result:.2f} Pounds")

            elif choice == '6':
                result = pound_to_kg(value)
                print(f"{value} Pounds = {result:.2f} KG")
        else:
            print("Invalid choice! Please select a number between 1 and 7.")

# Run the program
if __name__ == "__main__":
    unit_converter()