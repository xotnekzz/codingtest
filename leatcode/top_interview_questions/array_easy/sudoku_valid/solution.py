class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [ set() for _ in range(9) ]
        cols = [ set() for _ in range(9) ]
        boxes = [ set() for _ in range(9) ]
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                
                if v == ".":
                    continue
                
                box_idx = (r//3) * 3 + (c//3)
                
                if (v in rows[r] or v in cols[c] or v in boxes[box_idx]):
                    print(r)
                    print(c)
                    print(box_idx)
                    print(v)
                    return False
                rows[r].add(v)
                cols[c].add(v)
                boxes[box_idx].add(v)
        return True
                

if __name__ == "__main__":
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        [".", "1", ".", ".", "9", "5", ".", ".", "."],
        [".", "9", "2", ".", ".", ".", ".", "6", "."],
        [".", "6", ".", ".", ".", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", "8", "."],
        ["6", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(Solution().isValidSudoku(board))
