from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        merged = zip(values, labels)
        sort = sorted(merged, key=lambda x: x[0], reverse=True)
        used = {}
        num_used = 0
        total = 0
        for i in sort:
            if num_used < num_wanted:
                if i[1] not in used:
                    total += i[0]
                    used[i[1]] = 1
                    num_used += 1
                elif used[i[1]] < use_limit:
                    total += i[0]
                    used[i[1]] += 1
                    num_used += 1
        return total
