class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mirror = {
            "6": "9",
            "1": "1",
            "8": "8",
            "9": "6",
            "0": "0"
        }
        if len(num) == 1:
            return num == mirror.get(num, -1)
        i, j = 0, len(num) - 1
        while i <= j:
            if num[i] not in mirror or num[j] not in mirror:
                return False
            if mirror[num[i]] != num[j]:
                return False
            i += 1
            j -= 1
        return True
