class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        union = range(len(accounts))
        accountMap = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in accountMap:
                    accountMap[email] = i
                else:
                    parent = accountMap[email]
                    self.find(union, i, parent)
        emailgroup = {}
        for i in xrange(len(union)):
            group = union[i]
            if group not in emailgroup:
                emailgroup[group] = set(accounts[i][1:])
            else:
                emailgroup[group] = emailgroup[group].union(set(accounts[i][1:]))
        res = []
        for group in emailgroup.keys():
            name = accounts[group][0]
            data = [name] + sorted(list(emailgroup[group]))
            res.append(data)
        return res
    def find(self, union, child, parent):
        if parent != union[parent]:
            self.find(union, child, union[parent])
            return
        else:
            union[child] = parent
            return

s = Solution()
print s.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]])

# the difficult part is when a new account could be merge into 2 parents
# how could you also union 2 parents together