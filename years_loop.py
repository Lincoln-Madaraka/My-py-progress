year = eval(input("ENTER THE YEAR: "))

if year <= 1582:
  print("Not within the Gregorian calendar period")
elif year % 4 != 0 and year % 400 != 0:
 print("Common year")
elif year % 100 != 0:
 print("Leap year")
else:
 print("Leap year")
