class Solution:
    def firstOcc(self, nums, target):
        start, end = 0, len(nums) - 1
        ans = -1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                ans = mid
                end = mid - 1

        return ans

    def lastOcc(self, nums, target):
        start, end = 0, len(nums) - 1
        ans = -1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                ans = mid
                start = mid + 1

        return ans

    def searchRange(self, nums, target):
        first = self.firstOcc(nums, target)

        if first == -1:
            return [-1, -1]

        return [first, self.lastOcc(nums, target)]