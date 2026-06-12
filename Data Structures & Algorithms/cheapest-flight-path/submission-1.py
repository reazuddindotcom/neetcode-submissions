class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # create adj list X
        # create dist map
        # iterate k+1 times for each edge
        # VERY TRICKY: temp_price[e[1]] = min(temp_price[e[1]], price[e[0]]+e[2])

        INF = float("inf")
        price = [INF] * n
        price[src] = 0
        print(price)

        for i in range(k+1):
            # print("k", i)
            temp_price = list(price)
            for e in flights:
                # print("Edge", e)
                if price[e[0]] == INF:
                    # print("Continue for:", e[0])
                    continue
                # print("P", price)
                # print("T", temp_price, e[0], e[1], e[2])
                # VERY TRICKY
                temp_price[e[1]] = min(temp_price[e[1]], price[e[0]]+e[2])
                # print("T", temp_price)

            price = temp_price
            # print(price)

        if price[dst] == INF:
            return -1

        return price[dst]
        