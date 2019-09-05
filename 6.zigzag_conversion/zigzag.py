class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows
        inc = 1
        row_index = 0
        for i in range(len(s)):
            rows[row_index] += s[i]
            # if we reach both ends, we reverse the increase step
            if row_index == numRows-1 or (i != 0 and row_index == 0):
                inc = -inc
            row_index += inc
        return "".join(rows)
