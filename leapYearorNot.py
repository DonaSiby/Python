def leapYearOrNot(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return print("Leap Year")
  else:
    return print("Not Leap Year")

leapYearOrNot(2024)