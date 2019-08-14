class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        m = len(num1)
        n = len(num2)
        res = [0] * (m + n)
        # Step 1: get all one-digit products
        # Time complexity: O(n1*n2)
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                p1 = i + j  # the position index
                p2 = i + j + 1

                res[p1] += mul / 10
                res[p2] += mul % 10

        # Step 2: Sweep through the stored products with carry
        # Time complexity: O(n1+n2)
        carry = 0
        for i in xrange(m+n-1, -1, -1):
            temp = carry + res[i]
            carry, res[i] = temp / 10, str(temp % 10)
        return ''.join(res) if res[0] != '0' else ''.join(res[1:])


# https://discuss.leetcode.com/topic/30508/easiest-java-solution-with-graph-explanation
s = Solution()
print s.multiply('1','1')