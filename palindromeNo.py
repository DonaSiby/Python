def palindromeNo(num):
  num = str(num)
  if num == num[::-1]:
    return "Palindrome"
  else:
    return "Not Palindrome"
  
print(palindromeNo(121))
print(palindromeNo(123))