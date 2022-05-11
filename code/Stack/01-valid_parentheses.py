# EASY
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
#  determine if the input string is valid.
# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


inp = "[()[]{}]"

def isValid(s):
    stack = []
    bracketsMap = { ")":"(" , "}":"{" , "]":"[" }

    for c in s:
        if c in bracketsMap: 
            # if c is closing bracket
            if stack and stack[-1] == bracketsMap[c]: 
                # pop if stack is not empty and last element is opposite (opening) bracket
                stack.pop() 
            else: 
                # stack is empty : bracket doesn't match
                return False 
        else:
            # c is opening bracket
            stack.append(c) 

    return True if not stack else False # returning true or false based on if the stack is empty or not 


# print(isValid(inp))
