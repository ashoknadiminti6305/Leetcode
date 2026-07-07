class Solution:
    def sumAndMultiply(self, n: int) -> int:
        y = ""

        for ch in str(n):
            if ch != "0":
                y += ch

        if y == "":
            return 0

        num = int(y)
        digit_sum = sum(int(ch) for ch in y)

        return num * digit_sum