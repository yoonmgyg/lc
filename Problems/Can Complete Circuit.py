class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        profit = [gas[i] - cost[i] for i in range(len(gas))]
        max_station = 0
        max_gas = 0
        total = 0
        for station in range(len(profit)):
            total += profit[station]
            if profit[station] > max_gas:
                max_station = station
        
        return max_station if total >= 0 else -1
