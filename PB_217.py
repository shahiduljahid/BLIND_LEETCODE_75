class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = set()
        for n in nums:
            if n in hashMap:
                return True
            else:
                hashMap.add(n)
        return False
            
