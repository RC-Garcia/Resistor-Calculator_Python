# resistor_calculator.py

def calculate_needed_resistor(input_voltage, operating_current, load_resistance):
    """
    Calculate the needed resistor value based on input voltage, operating current, and load resistance.

    Parameters:
    - input_voltage (float): The input voltage in volts (V).
    - operating_current (float): The operating current in amperes (A).
    - load_resistance (float): The load resistance in ohms (Ω).

    Returns:
    - float: The calculated resistor value in ohms (Ω).
    """
    needed_resistor = (input_voltage - (operating_current * load_resistance)) / operating_current
    return needed_resistor

def main():
    print("Resistor Calculator")
    
    # Input values
    input_voltage = float(input("Enter the input voltage (V): "))
    operating_current = float(input("Enter the operating current (I): "))
    load_resistance = float(input("Enter the load resistance (R_L): "))
    
    # Calculate needed resistor
    needed_resistor = calculate_needed_resistor(input_voltage, operating_current, load_resistance)
    
    # Display result
    print(f"Needed Resistor: {needed_resistor:.2f} Ω")

if __name__ == "__main__":
    main()
