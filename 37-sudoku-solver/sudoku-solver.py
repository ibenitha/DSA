class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_space = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                box_idx = (r // 3) * 3 + (c // 3)

                if val != ".":
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
                else:
                    empty_space.append((r, c))

        def sudoku(idx):
            if idx == len(empty_space):
                return True

            r, c = empty_space[idx]
            box_idx = (r // 3) * 3 + (c // 3)

            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)

                    if sudoku(idx + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)

            return False

        sudoku(0)