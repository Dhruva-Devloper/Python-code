#by python librarrys 
from typing import List
import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1+nums2

        n = len(nums3)
        for i in range(n):       
              for j in range(n-1-i):
               if nums3[j] > nums3[j+1]:
                temp = nums3[j]
                nums3[j] = nums3[j+1]
                nums3[j+1] = temp
        return statistics.median(nums3)



obj = Solution()

print(obj.findMedianSortedArrays([1,3],[2]))
