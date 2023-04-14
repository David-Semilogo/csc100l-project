temperature_celcius = float(input("Enter Temperature in celcius: "))


if temperature_celcius < -273.15:
    print("The temperature is invalid because it is below absolute zero")
elif temperature_celcius == -273.15:
    print("The temperature is absolute 0")
elif temperature_celcius>-273.15 and temperature_celcius < 0:
    print("The temperature is below freezing")
elif temperature_celcius == 0:
    print("The temperature is at freezing point")
elif temperature_celcius>0 and temperature_celcius <100:
    print("The temperature is in normal range")
elif temperature_celcius == 100:
    print("The temperature is at boiling point")
else:
    print("The temperature is above boiling point")

