# MEDIUM
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
# This matrix has the following
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

def searchMatrix( matrix, target):
    row , col = len(matrix), len(matrix[0])
    top , bottom = 0, row-1

    while top <= bottom:
        mid = (top + bottom) //2

        if target > matrix[mid][-1]:
            top = mid + 1
        elif target < matrix[mid][0]:
            bottom = mid - 1
        else:
            break



   
matrix = [ [1,3,5,7],
           [10,11,16,20],
           [23,30,34,60] ]

# Output -> Boolean

searchMatrix(matrix, 3)