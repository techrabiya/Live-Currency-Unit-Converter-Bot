def elite_converter():
    print("=" * 50)
    print(" 💱 RABIA'S ELITE UNIT & CURRENCY CONVERTER 💱")
    print("=" * 50)
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. USD to INR (Estimated Rate: 83.0)")
    
    choice = input("Select conversion option (1/2/3): ").strip()
    
    if choice == '1':
        km = float(input("Enter kilometers: "))
        miles = km * 0.621371
        print(f"Result: {km} KM = {miles:.2f} Miles")
    elif choice == '2':
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"Result: {c}°C = {f:.2f}°F")
    elif choice == '3':
        usd = float(input("Enter amount in USD ($): "))
        inr = usd * 83.0
        print(f"Result: ${usd} USD = ₹{inr:.2f} INR")
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
    print("=" * 50)

if __name__ == "__main__":
    elite_converter()
