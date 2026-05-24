class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = set()
        ll = len(nums)
        # Assume at least 3 elements

        i = 0
        target = 0
        while i < ll:
            # print(i)
            start = i + 1
            end = ll - 1
            while start < end:
                summ = nums[i] + nums[start] + nums[end]
                if summ < target:
                    start += 1
                elif summ > target:
                    end -= 1
                else:
                    results.add((nums[i], nums[start], nums[end]))
                    # break # Shouldn't work. Might be a different combination.
                    start += 1
                    end -= 1

                    # LEARNING to avoid duplicates, don't skip i. Skip start and end.
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1

            i += 1
        
        return list(results)


# Input: nums=[0,0,0,0]
# Output: [[0,0,0],[0,0,0]]
# Expected: [[0,0,0]]

# nums: [-2,0,1,1,2]
# Output: [[-2,0,2]]
# Expected: [[-2,0,2],[-2,1,1]]
