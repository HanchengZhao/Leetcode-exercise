class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        letter = []
        for l in logs:
            first = l.split(" ")[1]
            if first.isnumeric():
                digit.append(l)
            else:
                letter.append(l)
        # we can put identifier in the last in case we have the same letters
        letter = sorted(letter, key=lambda x: " ".join(
            x.split(" ")[1:]) + x.split(" ")[0])
        return letter + digit
