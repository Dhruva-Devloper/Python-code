class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        degree = []
        for i in range(n) :
            count = len([x for x in matrix[i] if x!=0])
            degree.append(count)

        return degree
       

        

obj = Solution()

print(obj.findDegrees([[0,1,1],[1,0,1],[1,1,0]]))

print(obj.findDegrees([[0,1,0],[1,0,0],[0,0,0]]))

print(obj.findDegrees([[0]]))
        
