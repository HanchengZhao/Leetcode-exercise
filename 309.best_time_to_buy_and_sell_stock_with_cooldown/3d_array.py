class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        state = [[[0] * 2 for i in range(2)] for i in range(len(prices))]
        # i, j, k represents day, whether has stock, whether in the cool down period
        state[0][0][0], state[0][1][0] = 0, -prices[0]
        state[0][0][1], state[0][1][1] = 0, float("-inf")

        for i in range(1, len(prices)):
            # will only inherit from yesterday
            state[i][0][0] = max(state[i-1][0][0], state[i-1][0][1])
            # buy one new stock or hold one
            state[i][1][0] = max(state[i-1][0][0] -
                                 prices[i], state[i-1][1][0])
            # just sold from previous or today
            state[i][0][1] = max(state[i-1][1][0] + prices[i],
                                 state[i][1][0] + prices[i])
        return max(state[-1][0][0], state[-1][0][1])
