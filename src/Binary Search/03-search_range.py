# Input [3,3,3] 3
# Output [0,2]
# ! Incomplete had to be an O(logN) solution
def searchRange2(nums, target):
    res = []
        
    for i in range(len(nums)):
        if target == nums[i]:
            res.append(i)
    
    if len(res) == 1:
        res.append(res[0])

    if len(res) != 0:
        return [res[0],res[-1]]
    else:
        return [-1,-1]

print(searchRange([3,3,3], 3))

