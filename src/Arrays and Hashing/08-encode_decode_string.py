# MEDIUM
# Encode and Decode Strings
class Solution:
    def encode(self, strs):
        res = ""
        for w in strs:
            res += str(len(w)) + "#" + w
        
        print(res)
            


    def decode(self, str):
        res , i = [] , 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            charLen = int(str[i:j])
            tempStr = str[j+1 : j+1+charLen]
            res.append(tempStr)
            i = j + charLen + 1
            
        print(res)



Input = ["lint","code","love","you"]
de = "4#lint4#code4#love3#you"


obj = Solution()
# obj.encode(Input)
obj.decode(de)

