class Solution(object):    
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
       
        index, step = 0, 1
        result = [""] * numRows
        #go down and up in zig zag way
        for i in s:
            result[index] += i
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        
        print(''.join(result))
    
if __name__ == '__main__':
    Solution().convert("PAYPALISHIRING", 3)
    
            
            
            