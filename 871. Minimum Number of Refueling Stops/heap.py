import heapq


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        fuel = startFuel
        # stations index
        i = 0
        steps = 0
        while True:
            if fuel >= target:
                return steps
            # store fuel in the visited stations into the heap
            while i < len(stations) and stations[i][0] <= fuel:
                heapq.heappush(pq, -stations[i][1])
                i += 1
            if len(pq) == 0:
                break
            # stops at the station that gives the most fuel
            fuel += -heapq.heappop(pq)
            steps += 1
        return -1
