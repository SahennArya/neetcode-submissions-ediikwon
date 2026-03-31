class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for n in range (0,len(nums)):
            if target - nums[n] in nums and nums.index(target-nums[n]) != n:
                arr.append(n)
                arr.append(nums.index(target-nums[n]))
                break
        return sorted(arr)