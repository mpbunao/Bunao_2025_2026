def convert_to_celsius(temp, unit):
    if unit == "C":
        return temp
    elif unit == "F":
        return (temp - 32) * 5 / 9
    elif unit == "K":
        return temp - 273.15
    else:
        return None

def check_temperature(tempC):
    if tempC < 0:
        return "Too cold!"
    elif tempC > 35:
        return "Too hot!"
    else:
        return "Safe temperature"

def main():
    unit = input("Enter unit of measurement: ").upper()
    if unit not in ["C", "F", "K"]:
        print("Invalid")
        return
    
    try:
        temp = float(input("Enter temperature: "))
    except ValueError:
        print("Invalid input. Must be a number.")
        return
    
    tempC = convert_to_celsius(temp, unit)
    result = check_temperature(tempC)
    print(f"Temperature in Celsius: {tempC:.2f}°C")
    print(result)

if __name__ == "__main__":
    main()
