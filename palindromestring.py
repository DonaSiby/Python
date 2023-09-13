def palindromeString(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
string1="malayalam"
string2="python"

print(palindromeString(string1))
print(palindromeString(string2))