# Partition an array into three parts: less, equal or greater than some target value.
# Example of input: {2,1,2,5,0}, target = 2
# Example of output: {1,0,2,2,5}, or {0, 1, 2, 2, 5}


def arrange(nums, target):
    if len(nums) == 0:
        return
    less, equal, greater = 0, 0, 0
    for i in nums:
        if i < target:
            less += 1
        if i == target:
            equal += 1
        else:
            greater += 1
    # start point
    i, j, k = 0, less, less+equal
    p = 0
    while less and equal and greater and p != len(nums):
        # print(p, i, j, k)
        # print(nums)
        if nums[p] < target:
            nums[p], nums[i] = nums[i], nums[p]
            i += 1
            less -= 1
        if nums[p] == target:
            nums[p], nums[j] = nums[j], nums[p]
            j += 1
            equal -= 1
        if nums[p] > target:
            nums[p], nums[k] = nums[k], nums[p]
            k += 1
            greater -= 1
        if p != i and p != j:
            p += 1
    return nums


print(arrange([2, 1, 2, 5, 0], 2))
print(arrange([6, 5, 4, 3, 2, 3, 3, 3, 1], 3))
print(arrange([3, 3, 3, 2, 2, 2, 1, 1, 1], 2))
print(arrange([3], 2))
