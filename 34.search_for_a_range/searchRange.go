package searchRange
// use 2 binary searches to find the first and the last one
func searchRange(nums []int, target int) []int {
	low := 0
	high := len(nums) - 1
	first := -1
	last := -1
	// get the first position
	for low <= high {
			mid := low + (high - low) >> 1
			if nums[mid] == target {
					if mid == 0 || nums[mid-1] < target {
						first = mid
						break
					} else {
						// not the first one
						high = mid - 1
					}
			} else if nums[mid] < target {
				low = mid + 1
			} else {
				high = mid - 1
			}
	}
	low = 0
	high = len(nums) - 1
	// find the last one
	for low <= high {
		mid := low + (high - low) >> 1
		if nums[mid] == target {
			if mid == len(nums) - 1 || nums[mid+1] > target {
				last = mid
				break
			} else {
				low = mid + 1
			}
		} else if nums[mid] > target {
			high = mid -1
		} else {
			low = mid + 1
		}
	}
	res := []int {first, last}
	return res
}