
print("TRANSFORMER EFFICIENCY CALCULATOR")

input_power = float(input("Enter input power (W): "))
output_power = float(input("Enter output power (W): "))

if input_power <= 0:
    print("Input power must be positive.")

elif output_power < 0 or output_power > input_power:
    print("Please enter valid output power.")

else:
    losses = input_power - output_power
    efficiency = (output_power / input_power) * 100

    print("\n--- RESULTS ---")
    print("Input Power:", input_power, "W")
    print("Output Power:", output_power, "W")
    print("Power Loss:", losses, "W")
    print("Efficiency:", round(efficiency, 2), "%")
