class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_cols = len(matrix[0])
        num_rows = len(matrix)
        rows_num = -1
        left = 0
        right = num_rows - 1

        while left <= right:
            midpoint = (left + right) // 2

            if (target >= matrix[midpoint][0] and target <= matrix[midpoint][num_cols-1]):
                rows_num = midpoint
                break
            elif target < matrix[midpoint][0]:
                right = midpoint - 1
            else: 
                left = midpoint + 1
        
        if rows_num == -1:
            return False
        
        left = 0
        right = num_cols - 1
        while left <= right:
            midpoint = (left + right) // 2

            if target == matrix[rows_num][midpoint]:
                return True
            elif target > matrix[rows_num][midpoint]:
                left = midpoint + 1
            else: 
                right = midpoint - 1
        
        return False
