class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Q what if there are multiple starting stations possible ??
        if not gas or not cost or len(gas) != len(cost):
            return -1

        balance = []
        for i in range(len(gas)):
            balance.append(gas[i]-cost[i])

        cur_gas = 0
        i = 0
        j = 0
        total_gas = 0
        while j < len(balance):
            total_gas += balance[j]
            cur_gas += balance[j]
            j += 1
            if cur_gas < 0:
                cur_gas = 0
                i = j

        if total_gas >= 0:
            return i
        else:
            return -1
