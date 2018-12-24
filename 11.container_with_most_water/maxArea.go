package main

import "fmt"

// use two pointers "head" and "tail" to traverse the array
// if head is taller than tail, move tail towards head, otherwise move head towards tail
// calculate the area while moving the pointer and keep the maximum area value

func maxArea(height []int) int {
	maxArea := 0
	head := 0
	tail := len(height) - 1
	for head < tail {
		area := Min(height[head], height[tail]) * (tail - head)
		maxArea = Max(maxArea, area)
		fmt.Println("head, tail, area", head, tail, area)
		if height[head] < height[tail] {
			head++
		} else {
			tail--
		}
	}
	return maxArea
}

//Min return min number of two int
func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// Max return max number of two int
func Max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func main() {
	height := []int{1, 2, 3, 4}
	fmt.Println(maxArea(height))
}
