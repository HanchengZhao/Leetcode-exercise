class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = [0] * (num + 1)
        for i in range(1, num+1):
            # shift one 1 bit left and add least significant element
            bits[i] = bits[i >> 1] + (i & 1)
        return bits
