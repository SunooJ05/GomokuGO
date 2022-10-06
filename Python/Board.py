# black is 1 and white is 2

import AI as ai


class GomokuReferee:
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def __str__(self):
        for value in range(len(self.board)):
            print(self.board[value])

    def move(self, y, x, color):
        if self.board[x][y] == 0:
            self.board[x][y] = color

    def is_win(self, y, x):
        end_row = len(self.board)
        color = self.board[x][y]

        def check(values):
            counter = 0
            if color == 2:
                for value in values:
                    if value == color:
                        counter += 1
                    else:
                        counter = 0
                    if counter == 5:
                        return 1
                return 0
            if color == 1:
                max_counter = 0
                for value in values:
                    if value == color:
                        counter += 1
                    else:
                        counter = 0
                    if counter > max_counter:
                        max_counter = counter
                if max_counter == 5:
                    return 1
                elif max_counter < 5:
                    return 0
                elif max_counter > 5:
                    return -1

        if ((check([self.board[i][y] for i in range(max(0, x - 5 + 1), min(end_row, x + 5))])
             or (check([self.board[x][i] for i in range(max(0, y - 5 + 1), min(end_row, y + 5))]))
             or (check([self.board[x + i][y + i] for i in range(max(-x, -y, 1 - 5), min(end_row - x, end_row - y, 5))]))
             or (check([self.board[x + i][y - i] for i in
                        range(max(-x, y - end_row + 1, 1 - 5), min(end_row - x, y + 1, 5))]))) == 1):
            return 1
        elif ((check([self.board[i][y] for i in range(max(0, x - 5 + 1), min(end_row, x + 5))])
               or (check([self.board[x][i] for i in range(max(0, y - 5 + 1), min(end_row, y + 5))]))
               or (
               check([self.board[x + i][y + i] for i in range(max(-x, -y, 1 - 5), min(end_row - x, end_row - y, 5))]))
               or (check([self.board[x + i][y - i] for i in
                          range(max(-x, y - end_row + 1, 1 - 5), min(end_row - x, y + 1, 5))]))) == -1):
            return -1
        elif self.is33(x, y, color):
            if color == 1:
                return -1
        elif self.is44(x, y, color):
            if color == 1:
                return -1
        elif (check([self.board[i][y] for i in range(max(0, x - 5 + 1), min(end_row, x + 5))])
              or (check([self.board[x][i] for i in range(max(0, y - 5 + 1), min(end_row, y + 5))]))
              or (
              check([self.board[x + i][y + i] for i in range(max(-x, -y, 1 - 5), min(end_row - x, end_row - y, 5))]))
              or (check([self.board[x + i][y - i] for i in
                         range(max(-x, y - end_row + 1, 1 - 5), min(end_row - x, y + 1, 5))])) == 0):
            return 0

    def is_illegal_move(self, y, x, color):

        if self.is33(y, x, color) or self.is44(y,x,color):
            return True
        else:
            return False

    def is33(self, y, x, color):
        open_3_count = 0
        open_3_count += ai.three_finder1(self.board, y, x, color)
        open_3_count += ai.three_finder2(self.board, y, x, color)
        open_3_count += ai.three_finder3(self.board, y, x, color)
        open_3_count += ai.three_finder4(self.board, y, x, color)
        if open_3_count >= 2:
            return True
        else:
            return False



    def is44(self, y, x, color):
        four_count = 0
        four_count += ai.four_finder1(self.board, y, x, color)
        four_count += ai.four_finder2(self.board, y, x, color)
        four_count += ai.four_finder3(self.board, y, x, color)
        four_count += ai.four_finder4(self.board, y, x, color)
        if four_count >= 2:
            return True
        else:
            return False


