#selection Sorting program Basic

from typing import List

class Solution:
    def selectionsort(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            min_index = i

            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j

            nums[i], nums[min_index] = nums[min_index], nums[i]

        return nums


obj = Solution()
print(obj.selectionsort([64, 25, 12, 22, 11]))
