class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        if start > destination:
            start, destination = destination, start
        clock = sum(distance[start: destination])
        return max(clock, total-clock)
