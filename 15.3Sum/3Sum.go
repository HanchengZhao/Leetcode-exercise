package main

import (
	"fmt"
	"sort"
)

// 2 pointers solution
// time Complexity: O(n^2)
// spance complexity:
func threeSum(nums []int) [][]int {
	var res [][]int
	// edge condition
	if len(nums) < 3 {
		return res
	}
	sort.Ints(nums)
	for i := 0; i <= len(nums)-2; i++ {
		//avoid duplicate first elememnt
		if i == 0 || i != 0 && nums[i] != nums[i-1] {
			target := 0 - nums[i]
			lo := i + 1
			hi := len(nums) - 1
			for lo < hi {
				if nums[lo]+nums[hi] == target {
					s := []int{nums[i], nums[lo], nums[hi]}
					res = append(res, s)
					for lo < hi && nums[lo+1] == nums[lo] { // avoid duplicate lo value
						lo++
					}
					for lo < hi && nums[hi-1] == nums[hi] {
						hi--
					}
					lo++
					hi--
				} else if nums[lo]+nums[hi] < target {
					lo++
				} else if nums[lo]+nums[hi] > target {
					hi--
				}
			}
		}
	}
	return res
}

func main() {
	nums := []int{-1, 0, 1, 2, -1, -4}
	res := threeSum(nums)
	fmt.Printf("%v", res)
}
