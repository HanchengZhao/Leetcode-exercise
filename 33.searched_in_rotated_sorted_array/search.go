package search
func search(nums []int, target int) int {
	low := 0
	high := len(nums) - 1
	for low <= high {
			mid := low + (high - low) >> 1
			if nums[mid] == target { 
					return mid
			}
			// first half is sorted
			// don't forget the equal sign
			if nums[mid] >= nums[low] {
					
					// inside this section
					if target >= nums[low] && target < nums[mid] {
							high = mid - 1
					} else {
							low = mid + 1
					}
			} else {
					if target > nums[mid] && target <= nums[high] {
							low = mid + 1
					} else {
							high = mid - 1
					}
			} 
	}
	return -1
}