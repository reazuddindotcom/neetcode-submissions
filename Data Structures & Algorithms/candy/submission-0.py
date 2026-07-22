class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n  # Start with 1 candy for each child
        
        # Step 1: Create a list of (rating, index) pairs
        rating_index_pairs = [(ratings[i], i) for i in range(n)]
        
        # Step 2: Sort by rating (lowest to highest)
        rating_index_pairs.sort()
        
        # Step 3: Assign candies from lowest to highest rating
        for rating, idx in rating_index_pairs:
            # Check both neighbors and ensure current child has more candies if rating is higher
            if idx > 0 and ratings[idx] > ratings[idx - 1]:
                candies[idx] = max(candies[idx], candies[idx - 1] + 1)
            if idx < n - 1 and ratings[idx] > ratings[idx + 1]:
                candies[idx] = max(candies[idx], candies[idx + 1] + 1)
        
        return sum(candies)
        