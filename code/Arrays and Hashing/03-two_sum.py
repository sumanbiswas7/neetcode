# EASY
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

def hasSum(nums,target):
    hashSet = set()
    for i in nums:
        if target-i in hashSet:
            resVar = {nums.index(i),nums.index(target-i)}
            return resVar
        hashSet.add(i)
    return False

sampleArr = [1,3,2,6,20]
# hasSum(sampleArr, 23)
