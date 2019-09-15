class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        # mid = ""
        cur = ""
        # firstParen = True
        for i in s:
            if i == "(":
                stack.append(cur)
                cur = ""
            elif i == ")":
                last = stack.pop()
                reversed = cur[::-1]
                cur = last + reversed
            else:
                cur += i
            # print(stack, cur)
        return stack.pop() + cur if stack else cur


s = Solution()
print(s.reverseParentheses("(abcd)"))
print(s.reverseParentheses("(u(love)i)"))
print(s.reverseParentheses("(ed(et(oc))el)"))
print(s.reverseParentheses("a(bcdefghijkl(mno)p)q"))
print(s.reverseParentheses("abcdef"))
# should be "tauswa"
print(s.reverseParentheses("ta()usw((((a))))"))
print(s.reverseParentheses("usw(a)"))
