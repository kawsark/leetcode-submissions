class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsmap = {}
        for i in range(len(nums)):
            if nums[i] in numsmap:
                numsmap[nums[i]].append(i)
            else:
                numsmap[nums[i]] = [i]
        
        nums.sort()
        i = 0
        j = len(nums) - 1

        while i < j:
            sum = nums[i] + nums[j]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else: # This should be the solution
                break
        
        index1 = numsmap[nums[i]][0]
        index2 = numsmap[nums[j]][0]
        
        # Handle duplicate
        if nums[i] == nums[j]:
            index2 = numsmap[nums[j]][1]

        return [index1, index2]