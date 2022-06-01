# MEDIUM
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

def evalRPN(tokens):
    stack = []
    for i in tokens:
      if i == "+":
          stack.append(stack.pop() + stack.pop())
      elif i == "-":
          a , b = stack.pop() , stack.pop()
          stack.append(b - a)
      elif i == "*":
          stack.append(stack.pop() * stack.pop())
      elif i == "/":
          a , b = stack.pop() , stack.pop() 
          stack.append(int(b / a))
      else:
          stack.append(int(i))

    print(stack)
    return stack[0]

tokens = ["2","1","+","3","*"]
tokens2 = ["4","13","5","/","+"]
evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
