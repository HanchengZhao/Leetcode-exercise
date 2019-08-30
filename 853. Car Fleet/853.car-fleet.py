#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the cars based on the location
        cars = sorted(zip(position, speed), key=lambda x: x[0])
        times = [(target - p) / s for p, s in cars]
        fleet = 0
        while len(times) > 1:
            front = times.pop()
            # the front gets to the destination first
            if front < times[-1]:
                fleet += 1
            # the behind car gets slower arrival time
            else:
                times[-1] = front
        # if there's still one car remaining
        return fleet + bool(times)
