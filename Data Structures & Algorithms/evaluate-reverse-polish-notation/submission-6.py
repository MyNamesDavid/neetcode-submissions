
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums_container = []

        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                nums_container.append(int(i))
            else:
                digit2 = nums_container.pop()
                digit1 = nums_container.pop()

                nums_container.append(
                    self.aritamtic_helper(digit1, digit2, i)
                )

        return nums_container[-1]

    def aritamtic_helper(self, digit1, digit2, operand):
        if operand == "+":
            return digit1 + digit2
        elif operand == "-":
            return digit1 - digit2
        elif operand == "*":
            return digit1 * digit2
        else:
            return int(digit1 / digit2)
