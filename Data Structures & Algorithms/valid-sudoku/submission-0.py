class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        box = [[False] * 9 for _ in range(9)]


        for i in range(9):
          for n in range(9):

            num = board[i][n]
            if num == ".":
                continue

            digit_index = int(num) -1 

            box_index = (i // 3) * 3 + (n // 3)

            if rows[i][digit_index] or cols[digit_index][n] or box[box_index][digit_index]:
              return False

            rows[i][digit_index] = True
            cols[digit_index][n] = True
            box[box_index][digit_index] = True

        return True