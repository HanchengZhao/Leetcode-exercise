'''
A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.

Note:

A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.
'''

from collections import defaultdict


class Solution:
    def minTransfers(self, transactions) -> int:
        debts = defaultdict(int)
        for x, y, z in transactions:
            debts[x] -= z
            debts[y] += z

        balances = list(debts.values())

        def dfs(s):
            while s < len(balances) and balances[s] == 0:
                s += 1
            if s == len(balances):
                return 0
            min_transactions = float("inf")
            for i in range(s+1, len(balances)):
                if balances[i] * balances[s] < 0:
                    balances[i] += balances[s]
                    min_transactions = min(min_transactions, 1 + dfs(s + 1))
                    balances[i] -= balances[s]
            return min_transactions
        return dfs(0)


'''
Backtrack each person's balance. For every pair of people, we clear the balance of the first person, then move to the 
next, in the mean time, append the balance back and check next one.

'''

transactions = [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]
s = Solution()
print(s.minTransfers(transactions))
