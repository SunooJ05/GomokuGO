# black is 1 and white is 2

import AI as ai


class GomokuReferee:
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        open_3_count += self.three_finder1(y, x, color)
        open_3_count += self.three_finder2(y, x, color)
        open_3_count += self.three_finder3(y, x, color)
        open_3_count += self.three_finder4(y, x, color)
        if open_3_count >= 2:
            return True
        else:
            return False

    def three_finder1(self, x, y, color):
        right_stone_count = 0
        left_stone_count = 0
        blank_count_left = 0
        if color == 1:
            opponent_color = 2
        else:
            opponent_color = 1

        delta_x = x-1
        while True:

            if delta_x == -1:
                break
            if self.board[y][delta_x] == color:
                left_stone_count += 1
            elif self.board[y][delta_x] == 0:
                if delta_x - 1 == -1:
                    break
                if self.board[y][delta_x-1] == 0:
                    break
                if blank_count_left == 1:
                    break
                blank_count_left += 1
            else:
                break
            delta_x -= 1

        blank_count_right = blank_count_left
        delta_x = x + 1
        while True:
            if delta_x == 15:
                break
            if self.board[y][delta_x] == color:
                right_stone_count += 1
            elif self.board[y][delta_x] == 0:
                if delta_x + 1 == 15:
                    break
                if self.board[y][delta_x + 1] == 0:
                    break
                if blank_count_right == 1:
                    break
                blank_count_right += 1
            else:
                break
            delta_x += 1

        all_stone_count = right_stone_count + left_stone_count
        if all_stone_count != 2:
            return 0
        left = left_stone_count + blank_count_left
        right = right_stone_count + blank_count_right
        if x-left == 0 or x+right == 15:
            return 0
        elif self.board[x-left-1][y] == opponent_color or self.board[x+right+1][y] == opponent_color:
            return 0
        else:
            return 1

    def three_finder2(self, x, y, color):
        up_stone_count = 0
        down_stone_count = 0
        blank_count_down = 0
        if color == 1:
            opponent_color = 2
        else:
            opponent_color = 1

        delta_y = y - 1
        while True:
            if delta_y == -1:
                break
            if self.board[delta_y][x] == color:
                down_stone_count += 1
            elif self.board[delta_y][x] == 0:
                if delta_y - 1 == -1:
                    break
                if self.board[delta_y-1][x] == 0:
                    break
                if blank_count_down == 1:
                    break
                blank_count_down += 1
            else:
                break
            delta_y -= 1

        blank_count_up = blank_count_down
        delta_y = y + 1
        while True:
            if delta_y == 15:
                break
            if self.board[delta_y][x] == color:
                up_stone_count += 1
            elif self.board[delta_y][x] == 0:
                if delta_y + 1 == 15:
                    break
                if self.board[delta_y+1][x] == 0:
                    break
                if blank_count_up == 1:
                    break
                blank_count_up += 1
            else:
                break
            delta_y += 1

        all_stone_count = up_stone_count + down_stone_count
        if all_stone_count != 2:
            return 0
        down = down_stone_count + blank_count_down
        up = up_stone_count + blank_count_up
        if x - down == 0 or x + up == 15:
            return 0
        elif self.board[x][y - down -1] == opponent_color or self.board[x][y + up +1] == opponent_color:
            return 0
        else:
            return 1

    def three_finder3(self, x, y, color):
        dr_stone_count = 0
        ul_stone_count = 0
        blank_count_ul = 0
        if color == 1:
            opponent_color = 2
        else:
            opponent_color = 1

        delta_x = x - 1
        delta_y = y - 1
        while True:
            if delta_x == -1 or delta_y == -1:
                break
            if self.board[delta_y][delta_x] == color:
                ul_stone_count += 1
            elif self.board[delta_y][delta_x] == 0:
                if delta_x - 1 == -1 or delta_y == -1:
                    break
                if self.board[delta_y - 1][delta_x - 1] == 0:
                    break
                if blank_count_ul == 1:
                    break
                blank_count_ul += 1
            else:
                break
            delta_x -= 1
            delta_y -= 1

        blank_count_dr = blank_count_ul
        delta_x = x + 1
        delta_y = y + 1
        while True:
            if delta_x == 15 or delta_y == 15:
                break
            if self.board[delta_y][delta_x] == color:
                dr_stone_count += 1
            elif self.board[delta_y][delta_x] == 0:
                if delta_x + 1 == 15 or delta_y + 1 == 15:
                    break
                if self.board[delta_y + 1][delta_x + 1] == 0:
                    break
                if blank_count_dr == 1:
                    break
                blank_count_dr += 1
            else:
                break
            delta_x += 1
            delta_y += 1

        all_stone_count = dr_stone_count + ul_stone_count
        if all_stone_count != 2:
            return 0
        ul = ul_stone_count + blank_count_ul
        dr = dr_stone_count + blank_count_dr
        if x - ul == 0 or x + dr == 15 or y - ul == 0 or y + dr == 15:
            return 0
        elif self.board[x - ul - 1][y - ul - 1] == opponent_color or self.board[x + dr + 1][y + dr + 1] == opponent_color:
            return 0
        else:
            return 1

    def three_finder4(self, x, y, color):
        dl_stone_count = 0
        ur_stone_count = 0
        blank_count_ur = 0
        if color == 1:
            opponent_color = 2
        else:
            opponent_color = 1

        delta_x = x + 1
        delta_y = y - 1
        while True:
            if delta_x == 15 or delta_y == -1:
                break
            if self.board[delta_y][delta_x] == color:
                ur_stone_count += 1
            elif self.board[delta_y][delta_x] == 0:
                if delta_x + 1 == 15 or delta_y == -1:
                    break
                if self.board[delta_y - 1][delta_x + 1] == 0:
                    break
                if blank_count_ur == 1:
                    break
                blank_count_ur += 1
            else:
                break
            delta_x += 1
            delta_y -= 1

        blank_count_dl = blank_count_ur
        delta_x = x - 1
        delta_y = y + 1
        while True:
            if delta_x == 0 or delta_y == 15:
                break
            if self.board[delta_y][delta_x] == color:
                dl_stone_count += 1
            elif self.board[delta_y][delta_x] == 0:
                if delta_x - 1 == 0 or delta_y + 1 == 15:
                    break
                if self.board[delta_y + 1][delta_x - 1] == 0:
                    break
                if blank_count_dl == 1:
                    break
                blank_count_dl += 1
            else:
                break
            delta_x -= 1
            delta_y += 1

        all_stone_count = dl_stone_count + ur_stone_count
        if all_stone_count != 2:
            return 0
        ur = ur_stone_count + blank_count_ur
        dl = dl_stone_count + blank_count_dl
        if x - dl == 0 or x + ur == 15 or y - dl == 0 or y + ur == 15:
            return 0
        elif self.board[x - dl - 1][y + ur + 1] == opponent_color or self.board[x + dl + 1][y - ur - 1] == opponent_color:
            return 0
        else:
            return 1

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


