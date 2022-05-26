# MEDIUM

# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


def productExceptSelf(nums):
    # O(1) memory
    res = [1] * len(nums)

    prefix = 1
    for i in range (len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= postfix
        postfix *= nums[i]
    
    return res


def productExceptSelf2(nums):
    # O (n) memory
    prefix = []
    i , j = 0, len(nums)-1
    m = 1
    while i < len(nums):
        m = m * nums[i]
        prefix.append(m)
        i += 1

    n = 1
    postfix = []
    while j >= 0:
        n = n * nums[j]
        postfix.append(n)
        j -= 1
    postfix.reverse()
    
    res = []
    k = 0
    for k in range(len(nums)):
        if k == 0:
            res.append(1 * postfix[1])
        elif k == len(nums)-1:
            res.append(prefix[k-1] * 1)
        else:
            res.append(prefix[k-1] * postfix[k+1])
    return res;  
        


InputNums = [1,2,3,4]
productExceptSelf(InputNums)
