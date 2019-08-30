from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions):
        invalids = set()
        names = defaultdict(list)
        for trans in transactions:
            name, time, amount, city = trans.split(",")
            for prevs in names[name]:
                n, t, a, c = prevs.split(",")
                if abs(int(t)-int(time)) <= 60 and c != city:
                    invalids.add(trans)
                    invalids.add(prevs)
            if int(amount) > 1000:
                invalids.add(trans)
            names[name].append(trans)
        return list(invalids)


s = Solution()

print(s.invalidTransactions(
    ["bob,627,1973,amsterdam", "alex,387,885,bangkok", "alex,355,1029,barcelona", "alex,587,402,bangkok", "chalicefy,973,830,barcelona", "alex,932,86,bangkok", "bob,188,989,amsterdam"]))
