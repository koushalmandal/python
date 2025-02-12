def palindrome(string):
    if string == string[::-1]:
      return "The string is palindrome"
    else:
      return "The string is not palindrome"
n=input("enter the string")
print(palindrome("mam"))
