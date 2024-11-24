def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def main():
    print("Welcome to the Temperature Converter!")
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        
        print("Choose the scale to convert to:")
        print("1. Fahrenheit")
        print("2. Kelvin")
        print("3. Both")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
        elif choice == "2":
            kelvin = celsius_to_kelvin(celsius)
            print(f"{celsius}°C is equal to {kelvin:.2f} K.")
        elif choice == "3":
            fahrenheit = celsius_to_fahrenheit(celsius)
            kelvin = celsius_to_kelvin(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F and {kelvin:.2f} K.")
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter a valid number for Celsius.")

if __name__ == "__main__":
    main()
