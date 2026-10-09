class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position,speed))
        pairs.sort(reverse = True)

        fleets = 1
        time1 = (target - pairs[0][0]) / pairs[0][1]

        for pos, speed in pairs:
            time2 = (target - pos) / speed
            if time1 < time2:
                fleets += 1
                time1 = time2
        return fleets

        