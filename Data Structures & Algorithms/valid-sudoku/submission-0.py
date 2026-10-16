
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = {}
        col_dict = {}
        box_dict = {}

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j].isdigit():
                    number = int(board[i][j])

                    if i not in row_dict:
                        row_dict[i] = [number]
                    elif number in row_dict[i]:
                        return False
                    else:
                        row_dict[i].append(number)

                    if j not in col_dict:
                        col_dict[j] = [number]
                    elif number in col_dict[j]:
                        return False
                    else:
                        col_dict[j].append(number)
                
                    box = (i // 3, j // 3)

                    if box not in box_dict:
                        box_dict[box] = []
                    if number in box_dict[box]:
                        return False
                    box_dict[box].append(number)

        return True
