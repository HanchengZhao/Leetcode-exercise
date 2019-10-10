class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_tank, Sum, pos = 0, 0, 0
        for i in range(len(gas)):
            cur_tank += gas[i] - cost[i]
            # reset
            if cur_tank < 0:
                Sum += cur_tank
                cur_tank = 0
                pos = i + 1
        Sum += cur_tank
        return -1 if Sum < 0 else pos


'''
time: O(n), space: O(1)
Calculate current tank for each step, update it to be 0 if cur_tank < 0, and update sum and pos to be i + 1.
In the end, if the total sum of gas and cost is bigger than 0, then there is a solution, othersize -1
'''
