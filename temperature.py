temp_number = int(input("Enter yout Teperature: "))

temp_type = input("Enter the Temperature unit in Celsius(C) or Fahrenheit(F)): ")

temp_type = temp_type.lower()

if temp_type == "f" or temp_type == "fahrenheit":
    result = (59*(temp_number - 32),"C","Celsius")
else:
    result = ((5 * temp_number) +32,"F","Fahrenheit")


print(f"Your Temperature in {result[2]} is {result[0]} {result[1]}")
