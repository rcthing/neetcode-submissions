class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position,speed))
        pairs.sort(reverse = True)

        fleets = 1
        time1 = (target - pairs[0][0]) / pairs[0][1]

        for i in range(1, len(pairs)):
            time2 = (target - pairs[i][0]) / pairs[i][1]
            if time1 < time2:
                fleets += 1
                time1 = time2
        return fleets

        