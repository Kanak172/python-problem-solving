class Solution(object):
    def removeDuplicates(self, nums):
        digit = -101

        list_a = []

        for i in nums : 
            if i != digit : 
                digit = i
                list_a.append(i)
            
        for i in range(len(list_a)):
            nums[i] = list_a[i]

        return len(list_a)