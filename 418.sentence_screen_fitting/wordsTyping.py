class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        count = 0
        row, col = 0, 0
        index = 0
        length = len(sentence)
        # res = ["" for i in range(rows+1)]
        while row < rows and col <= cols:
            if len(sentence[index]) <= cols - col:
                col +=  len(sentence[index])
                # res[row] += sentence[index]
            else: #no place for next word in this row
                row += 1
                # res[row] += sentence[index]
                col = len(sentence[index])
            if col < cols and col != 0:
                col += 1 #add a space
                # res[row] += "-"
            if row == rows:
                break
            index += 1
            #update count and index
            count += (index / length)
            index %= length
        # print res
        return count

s = Solution()
print s.wordsTyping(["try","to","be","better"], 10000, 9001)