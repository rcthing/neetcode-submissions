class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position,speed), reverse = True)

        fleets = 0
        time1 = 0

        for pos, spd in pairs:
            time2 = (target - pos) / spd
            if time1 < time2:
                fleets += 1
                time1 = time2
        return fleets

        