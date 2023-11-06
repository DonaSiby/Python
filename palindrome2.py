def palindrome(str):
  reversedString = ""
  for char in str:
    reversedString = char + reversedString
  print(reversedString)
  

str = "hi"
palindrome(str)
