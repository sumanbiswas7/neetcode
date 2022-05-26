# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

nums = [1,1,1,2,2,3]

def topKFrequent(nums, k):
    count = {}
    arr = [[] for i in range(len(nums) + 1)]

    for i in nums:
        count[i] = 1 + count.get(i , 0)

    for n , c in count.items():
        arr[c].append(n)

    res = []
    for i in range(len(arr)-1, 0, -1):
        for j in arr[i]:
            res.append(j)
        if len(res) == k:
            print(res)
            return res

