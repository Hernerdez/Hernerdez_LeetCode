# Problem: 36. Valid Sudoku
# Difficulty: Medium
# Pattern: HashMap/HashSet - checking for duplicates in constrained regions

"""
Key Insights:
1. We need to validate 3 things: rows, columns, and 3x3 sub-boxes
2. Only filled cells (non '.') need validation
3. We're checking for duplicates, not completeness
4. Sub-box formula: box_index = (row // 3) * 3 + (col // 3)
"""

# Approach 1: Brute Force - Check each constraint separately
# Time: O(9²) = O(81) = O(1) since board is fixed size
# Space: O(9) for the sets we create for each check
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Check all rows
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] != '.':
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        # Check all columns
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] != '.':
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        # Check all 3x3 sub-boxes
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                # Iterate through each cell in the 3x3 box
                for i in range(3):
                    for j in range(3):
                        row = box_row * 3 + i
                        col = box_col * 3 + j
                        if board[row][col] != '.':
                            if board[row][col] in seen:
                                return False
                            seen.add(board[row][col])

        return True


# Approach 2: Optimized Single Pass with HashSets
# Time: O(9²) = O(1) since board is fixed size
# Space: O(9²) = O(1) for storing all seen values
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Use sets to track seen numbers in each row, column, and box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]

                # Skip empty cells
                if val == '.':
                    continue

                # Calculate which 3x3 box this cell belongs to
                # box_index goes from 0-8 (left to right, top to bottom)
                box_index = (row // 3) * 3 + (col // 3)

                # Check if this value already exists in row, col, or box
                if val in rows[row] or val in cols[col] or val in boxes[box_index]:
                    return False

                # Add value to the respective sets
                rows[row].add(val)
                cols[col].add(val)
                boxes[box_index].add(val)

        return True


# Approach 3: Most Concise - Using single set with encoded positions
# Time: O(9²) = O(1)
# Space: O(9²) = O(1)
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    # Encode each constraint as a unique string
                    row_check = f"row{i}-{val}"
                    col_check = f"col{j}-{val}"
                    box_check = f"box{i//3}{j//3}-{val}"

                    # If any encoding already exists, we have a duplicate
                    if row_check in seen or col_check in seen or box_check in seen:
                        return False

                    seen.add(row_check)
                    seen.add(col_check)
                    seen.add(box_check)

        return True


# Example walkthrough with Approach 2:
# Input: board[0][0] = "5"
# Step 1: row = 0, col = 0, val = "5"
# Step 2: box_index = (0//3)*3 + (0//3) = 0*3 + 0 = 0
# Step 3: Check if "5" in rows[0]? No
#         Check if "5" in cols[0]? No
#         Check if "5" in boxes[0]? No
# Step 4: Add "5" to rows[0], cols[0], boxes[0]
# Continue for all cells...
#
# When we reach board[3][0] = "8":
# box_index = (3//3)*3 + (0//3) = 1*3 + 0 = 3
# This is a different box than board[0][0], so no conflict yet
#
# The key insight: box_index formula maps each cell to correct box:
# Boxes:  0 1 2
#         3 4 5
#         6 7 8


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Valid board
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    # Test case 2: Invalid board (two 8s in top-left box)
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    print(f"Test 1 - Expected: True, Got: {solution.isValidSudoku(board1)}")
    print(f"Test 2 - Expected: False, Got: {solution.isValidSudoku(board2)}")