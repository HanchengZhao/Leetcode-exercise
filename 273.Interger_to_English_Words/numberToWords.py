class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        lessThan20 = 'One Two Three Four Five Six Seven Eight Nine Ten' \
        'Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split(" ")
        tens = 'Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split(" ")
        thousands = ' Thousand Million Billion'.split(" ")

        def helper(num): # recursively handle the number < 1000
            print num
            if not num:
                return ""
            elif num < 20:
                return lessThan20[num - 1] + " "
            elif num < 100:
                return tens[num / 10 - 1] + " " + helper(num % 10)
            return lessThan20[num / 100 - 1] + " Hundred " + helper(num % 100)
        
        if not num:
            return 'Zero'
        words = ''
        i = 0 # count the thousands

        while num > 0:
            if num % 1000 > 0:
                words = helper(num % 1000) + thousands[i] + " " + words
            num /= 1000
            i += 1
        return words.strip()
        
    

s = Solution()
# print s.numberToWords(123456)
print s.numberToWords(134134123)