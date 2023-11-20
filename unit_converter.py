def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    print("Welcome to the Temperature Converter!")
    
    # Get user input
    try:
        value = float(input("Enter the temperature value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    
    print("\nChoose the source unit:")
    print("1. Celsius")
    print("2. Fahrenheit")
    
    try:
        source_unit = int(input("Enter the corresponding number for the source unit: "))
        if source_unit not in [1, 2]:
            print("Invalid source unit. Please enter 1 or 2.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    print("\nChoose the target unit:")
    print("1. Celsius")
    print("2. Fahrenheit")
    
    try:
        target_unit = int(input("Enter the corresponding number for the target unit: "))
        if target_unit not in [1, 2]:
            print("Invalid target unit. Please enter 1 or 2.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    # Perform the conversion
    if source_unit == 1 and target_unit == 2:
        result = celsius_to_fahrenheit(value)
        print(f"\nConverting {value} Celsius to Fahrenheit...")
        print(f"Result: {result} Fahrenheit")
    elif source_unit == 2 and target_unit == 1:
        result = fahrenheit_to_celsius(value)
        print(f"\nConverting {value} Fahrenheit to Celsius...")
        print(f"Result: {result} Celsius")
    else:
        print("Invalid source and target unit combination. Please choose Celsius to Fahrenheit or Fahrenheit to Celsius.")

# Run the temperature converter
temperature_converter()
