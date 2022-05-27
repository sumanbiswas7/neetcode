# MEDIUM
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
# This matrix has the following
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

def searchMatrix( matrix, target):
    top , bottom = 0 , len(matrix)-1

    while top <= bottom:
        mid = (top + bottom) // 2
        if target < matrix[mid][0]:
            bottom = mid - 1
        elif target > matrix[mid][-1]:
            top = mid + 1
        else:
            break
    
    if not top <= bottom:
        return False

    row = (top + bottom) // 2
    left , right = 0 , len(matrix[row]) - 1 
    while left <= right:
        mid = (left + right) // 2
        if target < matrix[row][mid]:
            right = mid - 1
        elif target > matrix[row][mid]:
            left = mid + 1
        else:
            return True
            
    return False



   
matrix = [ [1,3,5,7],
           [10,11,16,20],
           [23,30,34,60] ]

# Output -> Boolean

searchMatrix(matrix, 0)