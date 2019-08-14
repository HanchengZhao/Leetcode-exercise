class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = [0] * (num + 1)
        for i in range(1, num+1):
            # find the number that has one less 1 at last, then plus 1
            # it's garanteed that the number is in the array
            bits[i] = bits[i & (i-1)] + 1
        return bits
