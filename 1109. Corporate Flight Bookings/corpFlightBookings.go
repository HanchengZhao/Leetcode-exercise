// the idea is pretty straightforward, but the performance is not that good
// it takes O(len(bookings) * n)
func corpFlightBookings(bookings [][]int, n int) []int {
	res := make([]int, n)
	for _, booking := range bookings {
			for i:= booking[0]; i <= booking[1]; i++ {
					res[i-1] = res[i-1] + booking[2]
			}
	}
	return res
}