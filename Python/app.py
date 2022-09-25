from flask import Flask, request
import json
import sys
import Board

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!<a/p>"

@app.route("/tellMeWhatTodo",methods=['POST'])
def announce(): #lastStateJson : turn 1 or 2,lastPosition [x,y],board,withAI 0or1

    game = Board.Board()
    inputDic = json.loads(request.get_data())
    withAI = True if inputDic["withAI"] == 1 else False
    game.board = inputDic["board"]
    game.color = inputDic["turn"]
    lastPosition = inputDic["lastPosition"]
    lastY = lastPosition[0]
    lastX = lastPosition[1]

    answerX =-1
    answerY =-1

    returnDic={"winner":0,"answerPosition":[answerX,answerY]}

    if game.is_win(lastPosition[0],lastPosition[1]) == 1 : #사용자가 이겼는지 체크하는 함수
        returnDic["winner"] = game.color;
        return json.dumps(returnDic)
    elif game.is_win(lastPosition[0],lastPosition[1]) == -1 :
        if(game.color ==1):
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
