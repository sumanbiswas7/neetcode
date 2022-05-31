# MEDIUM

# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict

def groupAnagrams(strs):
    ans = defaultdict(list)
        
    for i in strs:
        count = [0] * 26    
        
        for s in i:
            count[ord(s)-ord("a")] += 1
            
        ans[tuple(count)].append(i)
        
    return ans.values()
                

def groupAnagrams2(strs):
    hashSet = {}
    n = 0
    for i in strs:
        tempStr = "".join(sorted(i))
        if not tempStr in hashSet:
            hashSet[tempStr] = n
            n += 1

    resArr = [[] for i in range(len(hashSet))]

    for i in range(len(strs)):
        tempStr = "".join(sorted(strs[i]))
        resArr[hashSet[tempStr]].append(strs[i])

    print(resArr)
    return resArr


strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)

