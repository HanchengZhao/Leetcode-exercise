import heapq

# Use a max-heap to keep track of the largest element.
# Since the remove operation takes O(k), so the time complexity is O(nk)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        res = []
        for i, val in enumerate(nums):
            if len(window) < k:
                # save negative value for max heap
                heapq.heappush(window, -val)
            else:
                window.remove(-nums[i-k])
                heapq.heapify(window)
                heapq.heappush(window, -val)
            if len(window) == k:
                # append the maximum
                res.append(-window[0])
        return res
