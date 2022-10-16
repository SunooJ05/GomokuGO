class AI:
    board = []
    y = 0
    x = 0
    x_ai = -1
    y_ai = -1

    def __init__(self, board, y, x):
        self.board = board
        self.y = y
        self.x = x

    def ai_input(self):

        self.has_four_opponent(self.board)
        self.has_four_own(self.board)
        return [self.x_ai, self.y_ai]

    def has_four_own(self, board):
        if four_finder1(board, self.y, self.x, 2) == 1:
            self.x_ai = ff1list[0]
            self.y_ai = ff1list[1]
        if four_finder2(board, self.y, self.x, 2) == 1:
            self.x_ai = ff2list[0]
            self.y_ai = ff2list[1]
        if four_finder3(board, self.y, self.x, 2) == 1:
            self.x_ai = ff3list[0]
            self.y_ai = ff3list[1]
        if four_finder4(board, self.y, self.x, 2) == 1:
            self.x_ai = ff4list[0]
            self.y_ai = ff4list[1]
    
    
    def has_four_opponent(self, board):
        if four_finder1(board, self.y, self.x, 1) == 1:
            self.x_ai = ff1list[0]
            self.y_ai = ff1list[1]
        if four_finder2(board, self.y, self.x, 1) == 1:
            self.x_ai = ff2list[0]
            self.y_ai = ff2list[1]
        if four_finder3(board, self.y, self.x, 1) == 1:
            self.x_ai = ff3list[0]
            self.y_ai = ff3list[1]
        if four_finder4(board, self.y, self.x, 1) == 1:
            self.x_ai = ff4list[0]
            self.y_ai = ff4list[1]


ff1list = [-1, -1]
ff2list = [-1, -1]
ff3list = [-1, -1]
ff4list = [-1, -1]


def four_finder1(board, y, x, color):
    right_stone_count = 0
    left_stone_count = 0
    blank_count_left = 0
    forced_end = 0
    if color == 1:
        opponent_color = 2
    else:
        opponent_color = 1
    delta_x = x - 1
    while True:
        if delta_x == -1:
            forced_end += 1
            break
        if board[y][delta_x] == color:
            left_stone_count += 1
        elif board[y][delta_x] == 0:
            if delta_x - 1 == -1:
                break
            if board[y][delta_x - 1] == 0:
                if ff1list[0] == ff1list[1] == -1:
                    ff1list[0] = y
                    ff1list[1] = delta_x
                break
            if blank_count_left == 1:
                break
            blank_count_left += 1
            ff1list[0] = y
            ff1list[1] = delta_x
        else:
            forced_end +=1
            break
        delta_x -= 1
    blank_count_right = blank_count_left
    delta_x = x + 1
    while True:
        if delta_x == 15:
            forced_end += 1
            break
        if board[y][delta_x] == color:
            right_stone_count += 1
        elif board[y][delta_x] == 0:
            if delta_x + 1 == 15:
                break
            if board[y][delta_x + 1] == 0:
                if ff1list[0] == ff1list[1] == -1:
                    ff1list[0] = y
                    ff1list[1] = delta_x
                break
            if blank_count_right == 1:
                break
            ff1list[0] = y
            ff1list[1] = delta_x
            blank_count_right += 1
        else:
            forced_end += 1
            break
        delta_x += 1
    all_stone_count = right_stone_count + left_stone_count
    if (blank_count_left == blank_count_right == 0) and forced_end == 2:
        return 0
    if all_stone_count == 3:
        return 1
    return 0


def four_finder2(board, y, x, color):
    up_stone_count = 0
    down_stone_count = 0
    blank_count_down = 0
    forced_end = 0
    if color == 1:
        opponent_color = 2
    else:
        opponent_color = 1

    delta_y = y - 1
    while True:
        if delta_y == -1:
            forced_end += 1
            break
        if board[delta_y][x] == color:
            down_stone_count += 1
        elif board[delta_y][x] == 0:
            if delta_y - 1 == -1:
                break
            if board[delta_y - 1][x] == 0:
                if ff2list[0] == ff2list[1] == -1:
                    ff2list[0] = delta_y
                    ff2list[0] = x
                break
            if blank_count_down == 1:
                break
            ff2list[0] = delta_y
            ff2list[1] = x
            blank_count_down += 1
        else:
            forced_end += 1
            break
        delta_y -= 1

    blank_count_up = blank_count_down
    delta_y = y + 1
    while True:
        if delta_y == 15:
            forced_end += 1
            break
        if board[delta_y][x] == color:
            up_stone_count += 1
        elif board[delta_y][x] == 0:
            if delta_y + 1 == 15:
                break
            if board[delta_y + 1][x] == 0:
                if ff2list[0] == ff2list[1] == -1:
                    ff2list[0] = delta_y
                    ff2list[0] = x
                break
            if blank_count_up == 1:
                break
            ff2list[0] = delta_y
            ff2list[1] = x
            blank_count_up += 1
        else:
            forced_end += 1
            break
        delta_y += 1

    all_stone_count = up_stone_count + down_stone_count
    if blank_count_down == blank_count_up == 0 and forced_end == 2:
        return 0
    if all_stone_count == 3:
        return 1
    return 0


def four_finder3(board, y, x, color):
    dr_stone_count = 0
    ul_stone_count = 0
    blank_count_ul = 0
    forced_end = 0
    if color == 1:
        opponent_color = 2
    else:
        opponent_color = 1

    delta_x = x - 1
    delta_y = y - 1
    while True:
        if delta_x == -1 or delta_y == -1:
            forced_end += 1
            break
        if board[delta_y][delta_x] == color:
            ul_stone_count += 1
        elif board[delta_y][delta_x] == 0:
            if delta_x - 1 == -1 or delta_y == -1:
                break
            if board[delta_y - 1][delta_x - 1] == 0:
                if ff3list[0] == ff3list[1] == -1:
                    ff3list[0] = delta_y
                    ff3list[1] = delta_x
                break
            if blank_count_ul == 1:
                break
            ff3list[0] = delta_y
            ff3list[1] = delta_x
            blank_count_ul += 1
        else:
            forced_end += 1
            break
        delta_x -= 1
        delta_y -= 1

    blank_count_dr = blank_count_ul
    delta_x = x + 1
    delta_y = y + 1
    while True:
        if delta_x == 15 or delta_y == 15:
            forced_end += 1
            break
        if board[delta_y][delta_x] == color:
            dr_stone_count += 1
        elif board[delta_y][delta_x] == 0:
            if delta_x + 1 == 15 or delta_y + 1 == 15:
                break
            if board[delta_y + 1][delta_x + 1] == 0:
                if ff3list[0] == ff3list[1] == -1:
                    ff3list[0] = delta_y
                    ff3list[0] = delta_x
                break
            if blank_count_dr == 1:
                break
            ff3list[0] = delta_y
            ff3list[1] = delta_x
            blank_count_dr += 1
        else:
            forced_end += 1
            break
        delta_x += 1
        delta_y += 1

    all_stone_count = dr_stone_count + ul_stone_count
    if blank_count_ul == blank_count_dr == 0 and forced_end == 2:
        return 0
    if all_stone_count == 3:
        return 1
    return 0


def four_finder4(board, y, x, color):
    dl_stone_count = 0
    ur_stone_count = 0
    blank_count_ur = 0
    forced_end =0
    if color == 1:
        opponent_color = 2
    else:
        opponent_color = 1

    delta_x = x + 1
    delta_y = y - 1
    while True:
        if delta_x == 15 or delta_y == -1:
            forced_end += 1
            break
        if board[delta_y][delta_x] == color:
            ur_stone_count += 1
        elif board[delta_y][delta_x] == 0:
            if delta_x + 1 == 15 or delta_y == -1:
                break
            if board[delta_y - 1][delta_x + 1] == 0:
                if ff4list[0] == ff4list[1] == -1:
                    ff4list[0] = delta_y
                    ff4list[0] = delta_x
                break
            if blank_count_ur == 1:
                break
            ff4list[0] = delta_y
            ff4list[1] = delta_x
            blank_count_ur += 1
        else:
            forced_end += 1
            break
        delta_x += 1
        delta_y -= 1

    blank_count_dl = blank_count_ur
    delta_x = x - 1
    delta_y = y + 1
    while True:
        if delta_x == 0 or delta_y == 15:
            forced_end += 1
            break
        if board[delta_y][delta_x] == color:
            dl_stone_count += 1
        elif board[delta_y][delta_x] == 0:
            if delta_x - 1 == 0 or delta_y + 1 == 15:
                break
            if board[delta_y + 1][delta_x - 1] == 0:
                if ff4list[0] == ff4list[1] == -1:
                    ff4list[0] = delta_y
                    ff4list[0] = delta_x
                break
            if blank_count_dl == 1:
                break
            ff4list[0] = delta_y
            ff4list[0] = delta_x
            blank_count_dl += 1
        else:
            forced_end += 1
            break
        delta_x -= 1
        delta_y += 1

    all_stone_count = dl_stone_count + ur_stone_count
    if blank_count_ur == blank_count_dl == 0 and forced_end == 2:
        return 0
    if all_stone_count == 3:
        return 1
    return 0


def three_finder1(board, y, x, color):
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
        if board[y][delta_x] == color:
            left_stone_count += 1
        elif board[y][delta_x] == 0:
            if delta_x - 1 == -1:
                break
            if board[y][delta_x-1] == 0:
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
        if board[y][delta_x] == color:
            right_stone_count += 1
        elif board[y][delta_x] == 0:
            if delta_x + 1 == 15:
                break
            if board[y][delta_x + 1] == 0:
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
    elif board[x-left-1][y] == opponent_color or board[x+right+1][y] == opponent_color:
        return 0
    else:
        return 1


def three_finder2(board, y, x, color):
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
        if board[delta_y][x] == color:
            down_stone_count += 1
        elif board[delta_y][x] == 0:
            if delta_y - 1 == -1:
                break
            if board[delta_y-1][x] == 0:
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
        if board[delta_y][x] == color:
            up_stone_count += 1
        elif board[delta_y][x] == 0:
            if delta_y + 1 == 15:
                break
            if board[delta_y+1][x] == 0:
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
    elif board[x][y - down -1] == opponent_color or board[x][y + up +1] == opponent_color:
        return 0
    else:
        return 1


def three_finder3(board, y, x, color):
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
        if board[delta_y][delta_x] == color:
            ul_stone_count += 1
        elif board[delta_y][delta_x] == 0:
            if delta_x - 1 == -1 or delta_y == -1:
                break
            if board[delta_y - 1][delta_x - 1] == 0:
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
        if board[delta_y][delta_x] == color:
            dr_stone_count += 1
        elif board[delta_y][delta_x] == 0:
            if delta_x + 1 == 15 or delta_y + 1 == 15:
                break
            if board[delta_y + 1][delta_x + 1] == 0:
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
    elif board[x - ul - 1][y - ul - 1] == opponent_color or board[x + dr + 1][y + dr + 1] == opponent_color:
        return 0
    else:
        return 1


def three_finder4(board, y, x, color):
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
        if board[delta_y][delta_x] == color:
            ur_stone_count += 1
        elif board[delta_y][delta_x] == 0:
            if delta_x + 1 == 15 or delta_y == -1:
                break
            if board[delta_y - 1][delta_x + 1] == 0:
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
        if board[delta_y][delta_x] == color:
            dl_stone_count += 1
        elif board[delta_y][delta_x] == 0:
            if delta_x - 1 == 0 or delta_y + 1 == 15:
                break
            if board[delta_y + 1][delta_x - 1] == 0:
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
    elif board[x - dl - 1][y + ur + 1] == opponent_color or board[x + dl + 1][y - ur - 1] == opponent_color:
        return 0
    else:
        return 1