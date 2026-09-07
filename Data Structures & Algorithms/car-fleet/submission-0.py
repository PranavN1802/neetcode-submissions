class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_ind = sorted(range(len(speed)), key=lambda i: position[i])

        fleet = 0
        pre_time = 0

        for idx in sorted_ind[::-1]:
            time_target = (target - position[idx]) / speed[idx]

            if time_target > pre_time:
                fleet += 1
                pre_time = time_target

        return fleet
        