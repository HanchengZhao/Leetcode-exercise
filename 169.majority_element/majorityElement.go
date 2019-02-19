func majorityElement(nums []int) int {
	var count, major int
	for i, ele := range nums {
		if i == 0 {
			major = ele
			count = 1
		} else if ele != major {
			count -= 1
			if count < 0 {
				major = ele
				count = 1
			}
		} else if ele == major {
			count += 1
		}
	}
	return major
}