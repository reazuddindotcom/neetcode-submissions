class Solution:
    def __init__(self):
        self.count_map = {}
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        # if amount == 0:
        #     return 0
        num_coins = [amount+1]*(amount+1)
        num_coins[0] = 0

        for i in range(1, amount+1, 1):
            for c in coins:
                if i - c >= 0:
                    num_coins[i] = min(num_coins[i], num_coins[i-c] + 1)

        if num_coins[amount] == amount+1:
            return -1

        return num_coins[amount]

        # COULDNT Figure out what is wrong
        # return self.minChange(coins, amount, 0, 0)

    def minChange(self, coins: List[int], amount: int, i: int, used: int) -> int:
        if amount == 0:
            return used

        if i >= len(coins) or amount < 0:
            return -1

        # This is wrong because, its just preventing further
        # exploration for the given remaining amount from index i
        # the first time cached value doesn't indicate the minimum
        # from all possible combination for the reamining amount
        if (amount, i) in self.count_map:
            print("Found", amount, i)
            print(self.count_map[(amount, i)])
            return self.count_map[(amount, i)]

        a = self.minChange(coins, amount-coins[i], i, used+1)

        b = self.minChange(coins, amount, i+1, used)

        result = -1
        if a < 0:
            result = b
        if b < 0:
            result = a
        else:
            result = min(a,b)

        # if result != -1:
        if (amount, i) not in self.count_map:
            self.count_map[(amount, i)] = result
            print("Added", amount, i, self.count_map[(amount, i)])
        else:
            self.count_map[(amount, i)] = min(result, self.count_map[(amount, i)])
            print("Updated", amount, i, self.count_map[(amount, i)])
        
        return result



# ----
# Yes, `if (amount, i) not in self.count_map` is correct for checking existence of a tuple key in a dictionary. Python tuples are hashable and can be used as dictionary keys, and the `in` operator works as expected.

# However, your overall approach has a **fundamental memoization problem** that will give incorrect results. Let me explain.

# ### The Issue: `used` spoils memoization

# Your `minChange` function returns the **total number of coins used from the root call** (because you add to `used` and pass it down). The returned value depends not only on `(amount, i)` but also on the **path taken to reach that state** (i.e., how many coins were already used). When you cache the result for `(amount, i)`, you store a value that includes the coins used **before** reaching that state. Later, if you reach the same `(amount, i)` via a different path (with a different `used` count), you return the cached value, which is incorrect.

# **Example**:  
# `coins = [1, 2]`, `amount = 3`  
# - Path A: use coin 1 (used=1) → coin 1 (used=2) → coin 1 (used=3) → state (amount=0, i=0) returns 3.  
# - Path B: use coin 2 (used=1) → state (amount=1, i=0) ...  
# If you cache the result for state (amount=1, i=0) from Path A (which is 3, because it took 2 more coins to finish), and later Path B reaches (amount=1, i=0) with `used=1`, it would incorrectly return 3, implying total coins = 1 + 3 = 4, which is wrong (actual minimum is 2).

# ### Fix: Don't pass `used` as a parameter

# Instead of accumulating coins used so far, let each recursive call return **the number of coins needed to complete the remaining amount from the current position**. Then the top-level call adds zero.

# **Correct structure**:
# ```python
# def minChange(self, amount, i):
#     if amount == 0:
#         return 0
#     if i >= len(coins) or amount < 0:
#         return -1
#     if (amount, i) in memo:
#         return memo[(amount, i)]
#     # take coin i
#     take = self.minChange(amount - coins[i], i)
#     if take != -1:
#         take += 1
#     # skip coin i
#     skip = self.minChange(amount, i + 1)
#     result = min(c for c in (take, skip) if c != -1) if any(v != -1 for v in (take, skip)) else -1
#     memo[(amount, i)] = result
#     return result
# ```

# Then in `coinChange`, call `self.minChange(amount, 0)`.

# ### Additional notes on your code

# - The condition logic for choosing `result` from `a` and `b` works, but is a bit fragile. The cleaner pattern above is safer.
# - The `__init__` and `self.count_map` are fine, but you could simply use `from functools import lru_cache` and decorate a helper function.
# - The `print` statements are helpful for debugging, but remove them eventually.
# - Time complexity with corrected memoization: O(amount * len(coins)). Space: O(amount * len(coins)).

# Your question about tuple key check is correct, but fixing the caching design is more urgent. Try restructuring as suggested, and test with small examples to see the difference.
# >>>
# You're right that both versions use an early return from cache, but the **meaning of the cached value** is different, which is why one breaks and the other doesn't.

# ### In your original code:
# ```python
# def minChange(self, amount, i, used):
#     if (amount, i) in self.count_map:
#         return self.count_map[(amount, i)]
# ```
# Here, `self.count_map[(amount, i)]` stores the **total number of coins used from the very beginning of the recursion**, i.e., the value of `used` at the time the state was first reached. But `used` depends on the **path** taken to reach `(amount, i)`. If you reach `(amount, i)` with `used=3` and cache `3`, later when you reach the same state via a different path with `used=2`, the cache returns `3`, which is wrong because the remaining work hasn't been accounted for separately. The cache entry incorrectly bundles the past path length.

# ### In the corrected structure:
# ```python
# if (amount, i) in memo:
#     return memo[(amount, i)]
# ```
# Here, `memo[(amount, i)]` stores **the minimum number of coins needed to finish the remaining amount starting from this state**, *excluding* any coins used before arriving here. Each call returns exactly the number of additional coins needed. This value depends only on `(amount, i)`, not on the path. So caching is valid.

# Both use early return, but the **semantics of the cached variable** differ:
# - Original: `cache[state] = total coins used so far` (path-dependent) → invalid.
# - Corrected: `memo[state] = additional coins needed from here` (path-independent) → valid.

# ### Why the corrected code doesn't suffer from the same issue
# When you reach `(amount, i)`, the number of coins needed to complete the amount is deterministic regardless of how you got there. So you can safely cache and return that value. In your original, the `used` parameter made the function's return value depend on the entire path, not just the state.

# Hope that clarifies the subtle but critical distinction!
