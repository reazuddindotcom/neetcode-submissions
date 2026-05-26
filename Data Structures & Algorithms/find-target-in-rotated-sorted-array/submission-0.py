class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return None

        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                # landed segment is already sorted
                # Or we just skipped the inflection point as its 
                # right between mid and mid+1
                #    . /
                #  /| /
                # / |/
                # [4,5,6,7,0,1,2]
                if nums[l] <= target and target <= nums[r]:
                    return self.sortedSearch(nums, l, r, target)

                
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid

            # '=' is needed if we keep landing on the left boundary
            # [2,1]
            if nums[l] <= nums[mid]:
                if nums[l] <= target and target <= nums[mid]:
                    return self.sortedSearch(nums, l, mid, target)
                l = mid + 1
            else:
                if nums[mid] <= target and target <= nums[r]:
                    return self.sortedSearch(nums, mid, r, target)
                r = mid - 1

        return -1
    
    def sortedSearch(self, nums: List[int], l: int, r: int, target: int) -> int:
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m

            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1