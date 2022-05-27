# MEDUIM

# You are given an integer array height of length n. There are n vertical lines drawn such
# that the two endpoints of the ith line are  (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49


def maxAreaB(height):
    # O(N^2)
    maxArea = 0
    for i in range(len(height)-1):
        for j in range(i+1,len(height)):
            tempArea = min(height[i], height[j]) * (j-i)
            maxArea = max(tempArea, maxArea)
    return maxArea

height = [1,8,6,2,5,4,8,3,7]

def maxArea(height):
    l , r = 0 , len(height)-1
    maxArea = 0
    while l < r:
        area = min(height[l],height[r]) * (r-l)
        maxArea = max(area, maxArea)
        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        else:
            l += 1

    return maxArea

maxArea(height)