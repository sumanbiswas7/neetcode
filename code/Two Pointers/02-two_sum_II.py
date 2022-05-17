# MEDIUM

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Your solution must use only constant extra space.

numbers = [2,7,11,15]
target = 9

def twoSum(numbers, target):
    l , r = 0 , len(numbers)-1
    while l < r:
        if numbers[l] + numbers[r] == target:
            print([l+1 , r+1])
            return [l+1 , r+1]
        elif numbers[l] + numbers[r] > target:
            r = r - 1
        elif numbers[l] + numbers[r] < target:
            l = l + 1
    return 0
        

twoSum(numbers, target)


