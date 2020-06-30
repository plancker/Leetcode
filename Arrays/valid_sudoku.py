class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        k = len(board)//3

        def containsDuplicate(nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            index = 1
            last = 0
            og_len = len(nums)

            nums.sort()

            while index < len(nums):
                if nums[index] == nums[last]:
                    nums.pop(index)
                else:
                    last = index
                    index = index + 1

            if og_len > len(nums):
                return True
            else:
                return False

        for row in range(len(board)):
            if containsDuplicate([int(x) for x in board[row] if x != "."]):
                return False

        for i in range(len(board)):
            col = [board[c][i] for c in range(len(board))]
            if containsDuplicate([int(x) for x in col if x != "."]):
                return False

        for box_no_row in range(0,len(board), 3):
            for box_no_col in range(0, len(board), 3):
                box = []
                for i in range(box_no_row, box_no_row+k):
                    for j in range(box_no_col, box_no_col+k):
                        box.append(board[i][j])
                if containsDuplicate([int(x) for x in box if x != "."]):
                    return False

        return True



X = Solution
print(X.isValidSudoku(X,  [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))