from flask import Flask, request
import json
import Board
import sys

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!<a/p>"

@app.route("/tellMeWhatTodo",methods=['POST'])
def announce(): #lastStateJson : turn 1 or 2,lastPosition [x,y],board,withAI 0or1

    inputDic = json.loads(request.get_data())


    game = Board.GomokuReferee()
    withAI = True if inputDic["withAI"] == 1 else False
    game.board = inputDic["board"]
    lastPosition = inputDic["lastPosition"]

    currentTurn = inputDic["turn"]
    # lastY = lastPosition[0]
    # lastX = lastPosition[1]

    answerX =-1
    answerY =-1

    returnDic={"winner":0,"answerPosition":[answerX,answerY]}

    if game.is_win(lastPosition[0],lastPosition[1]) == 1 : #사용자가 이겼는지 체크하는 함수
        returnDic["winner"] = currentTurn;
        return json.dumps(returnDic)
    elif game.is_win(lastPosition[0],lastPosition[1]) == -1 :
        if(currentTurn==1):
            returnDic["winner"] = 2
        else:
            returnDic["winner"] = 1
        return json.dumps(returnDic)

    #승자가 없다면
    if(withAI): # 여긴 나중에 선우 알고리즘 합침
        answerX = 1
        answerY = 1

    return json.dumps(returnDic)
    #returnDic : winner 0or1or2, answerPosition : [x,y]

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=False)