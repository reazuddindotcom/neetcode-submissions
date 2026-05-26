class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        l = 0
        r = len(nums) - 1
        min_v = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                # landed segment is already sorted
                # Or we just skipped the inflection point as its 
                # right between mid and mid+1
                #    . /
                #  /| /
                # / |/
                # [4,5,6,7,0,1,2]
                return min(min_v, nums[l])

                
            mid = l + (r-l) // 2
            min_v = min(nums[mid], min_v)
            # '=' is needed if we keep landing on the left boundary
            # [2,1]
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return min_v

# [2,1]. Changed "nums[l] < nums[mid]" to "nums[l] <= nums[mid]"
# Even in case of equal move to the other side

# [4,5,6,7,0,1,2]. Skipping the inflection point as its right between
# mid and mid+1

# if it was RIGHT to LEFT rotation, could the indexing be different??

