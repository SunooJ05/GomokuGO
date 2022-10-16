from Board import GomokuReferee
import AI as ai

def user_input():
    global x
    x = int(input("Enter x_value:"))
    global y
    y = int(input("Enter y_value:"))


def play():
    global color
    color = 1
    while True:
        #if color == 1:
        user_input()
        new_board.move(x,y, color)
        #elif color == 2:
            #ai.ai_input()
            #new_board.move(x, y, color)
        print("---------------------------------")
        new_board.__str__()
        if (new_board.is_win(x, y) == 1 and color == 1) or (new_board.is_win(x, y) == -1 and color == 2):
            print("Black Wins")
            break
        elif (new_board.is_win(x, y) == 1 and color == 2) or (new_board.is_win(x, y) == -1 and color == 1):
            print("White Wins")
            break
        if color == 1:
            color += 1
        elif color == 2:
            color -= 1


if __name__ == '__main__':
    new_board = GomokuReferee()
    new_board.__str__()
    play()

