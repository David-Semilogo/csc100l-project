length_cm = input("Enter your weight in cm: ")

length_cm = int(length_cm)

if length_cm<0:
    print("Entry is invalid")
else:
   result = length_cm/2.54
   print("Your length in inch is {:0.2f} inches".format(result))