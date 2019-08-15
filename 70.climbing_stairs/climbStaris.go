package climbstairs

func climbStairs(n int) int {
	if n == 1 {
		return 1
	}
	dp := make([]int, n+1)
	dp[0] = 1
	dp[1] = 1
	for i := 2; i <= n; i++ {
		dp[i] = dp[i-1] + dp[i-2]
	}
	return dp[n]
}

// use an array to memorize calculated stairs
