from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        #[3,9,7], k = 5
        n = len(nums)
        count = 0
        
        
        total = sum(nums)
        
        while total % k != 0 :
            total-=1
            count +=1
        return count

obj = Solution()

print(obj.minOperations([3,9,7],5))
