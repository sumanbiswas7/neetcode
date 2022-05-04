# EASY
# A phrase is a palindrome if, after converting all uppercase letters into lowercase 
# letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

testStr = "A man, a plan, a canal: Panama"

# Solution 1 
def isPalindrome(string):
    tempSrt = "" # using extra space 
    for char in string:
        if char.isalnum(): # depending on isalnum function
            tempSrt += char.lower()
    return tempSrt == tempSrt [::-1]

# print(isPalindrome(testStr))


# Solution 2
def isPalindrome2(string):
    l , r = 0 , len(string) - 1 

    while ( l < r ):
        while l < r and not isAlNum(string[l]):
            l = l+1
        while r > l and not isAlNum(string[r]):
            r = r-1
        if string[l].lower() != string[r].lower():
            return False
        l , r = l+1 , r-1
    return True 

def isAlNum(char):
    return (ord("A") <= ord(char) <= ord("Z") or 
            ord("a") <= ord(char) <= ord("z") or 
            ord("1") <= ord(char) <= ord("9")) # ord() char -> ASCII 

    return False

print(isPalindrome2(testStr))
