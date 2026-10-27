class Solution:
    def myPow(self, x: float, n: int) -> float:
        power = abs(n)
        result = 1.0

        while power:
            if power & 1:
                result *= x

            x *=x
            power >>= 1

        return result if n>=0 else 1.0 / result