class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        for i in nums:
            if list(nums).count(i) > 1:
                flag = True
                break
        return flag
        