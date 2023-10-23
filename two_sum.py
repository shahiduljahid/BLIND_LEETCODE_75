class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preamp = {} #val : index

        for i,n in enumerate(nums):
            diff = target - n
            if diff in preamp:
                return [preamp[diff],i]
            preamp[n]=i
        return
            
        