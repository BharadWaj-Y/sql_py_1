def isPalindrome(s):
    lastIndex = len(s)-1
    mid = len(s)//2
    for i in range(0,mid):
        if s[i] != s[lastIndex-i]:
         return False
    return True

s =input("Enter the word to check : ")
if isPalindrome(s):
    print("{} is a palindrome".format(s))
else:
     print("{} is not a palindrome".format(s))
