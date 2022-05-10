# EASY
# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

def search( nums, target):
    left, right = 0, len(nums)-1
    while (left < right):
        n = (left + right) // 2
        if nums[n] == target:
            return n
        elif nums[n] < target:
            left = n+1
        else:
            right = n-1
        
    return -1
def binarySearch(nums,target,l,r):
    n = (l+r)//2
    if r >= l:
        if nums[n] == target:
            print(n)
            return n
        elif nums[n] < target:
            return binarySearch(nums, target, n+1, r)
        else:
            return binarySearch(nums, target, l, n-1)
    else:
        return -1



test = [-1,0,3,5,9,12]

# print(search(test, 9))
binarySearch(test, 9, 0, 5)
