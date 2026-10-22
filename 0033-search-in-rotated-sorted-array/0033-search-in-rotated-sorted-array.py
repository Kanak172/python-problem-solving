class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            # Right half is sorted
            else:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1