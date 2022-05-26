# EASY
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

sampleArr = [2,45,1,5,44,70]

def hasDuplicate(nums: list[int]) -> bool():
    tempSet = set()
    for i in nums:
        if i in tempSet:
            return True
        tempSet.add(i)
    return False

# print(hasDuplicate(sampleArr)) 