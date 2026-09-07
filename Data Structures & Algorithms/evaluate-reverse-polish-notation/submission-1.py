class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            if item not in "+-*/":
                stack.append(int(item))
            else:
                op2 = stack.pop()
                op1 = stack.pop()

                if item == "+":
                    stack.append(op1 + op2)
                elif item == "-":
                    stack.append(op1 - op2)
                elif item == "*":
                    stack.append(op1 * op2)
                else:
                    stack.append(int(op1 / op2))

        return stack[0]
