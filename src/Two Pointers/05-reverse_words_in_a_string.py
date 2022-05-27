# MEDIUM
# Given an input string s, reverse the order of the words.
# Input: s = "the sky is blue"
# Output: "blue is sky the"

def reverseWords(s):
    # rem = " ".join(s.split())
    tempArr = []
    tempStr = ""

    l , i = 0 , len(s)-1
    while l <= i:

        if s[i] == " ":
            if tempStr != "":
                tempArr.append(tempStr)
            tempStr = ""
        elif i == 0:
            if s[i] == " ":
                if tempStr != "":
                    tempArr.append(tempStr)
            else:
                tempStr = s[i] + tempStr
                tempArr.append(tempStr)
        else:
            tempStr = s[i] + tempStr

        i -= 1

    res = " ".join(tempArr)
    return res
   

reverseWords("the sky is blue")
