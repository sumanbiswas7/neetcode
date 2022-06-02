# MEDIUM
# ! LEARN BACKTRACKING FIRST
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

def generateParenthesis(n):
    res = []
    stack = []

    def backtrack(openC , closeC):
        if openC == closeC == n:
            print("open == close = ",openC ,("".join(stack)))

        if openC < n:
            print("open < n - " ,stack)
            stack.append("(")
            print("append - " ,stack)
            backtrack(openC + 1, closeC)
            print("backtracking done")
            stack.pop()

        if closeC < openC:
            print("close < openC - " ,stack)
            stack.append(")")
            print("append - " ,stack)
            backtrack(openC, closeC + 1)
            print("backtracking done")
            stack.pop()

    backtrack(0, 0)

generateParenthesis(2)
