import 'dart:convert';
import 'dart:io';

import 'package:SWGOMOKUGO/constant.dart';
import 'package:SWGOMOKUGO/painter/board.dart';
import 'package:SWGOMOKUGO/painter/piece.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SW GOMOKUGO',
      theme: ThemeData(
        primarySwatch: Colors.indigo,
      ),
      home: const MyHomePage(title: 'SW GOMOKUGO'),
      debugShowCheckedModeBanner: false,
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  var checkBoard = List.generate(kan, (i) => List.generate(kan,(j)=>0), growable: false);
  var currentPlayer = 1;
  var chickenDinner = 0;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Center(child: Text(widget.title)),
        elevation: 0,
      ),
      body: Center(
        child : Stack(
          alignment: Alignment.center,
          children: [
            GestureDetector(
              onTapUp:(TapUpDetails details){
                putPiece(details.localPosition,context);
              },

              child: CustomPaint(
                size: Size(boardHeight, boardWidth),
                painter : Board(),
                child: CustomPaint(
                  size: Size(boardHeight, boardWidth),
                  painter: Piece(checkBoard),
                ),
              ),
            ),
            chickenDinner!=0?Container(
              width: boardWidth*0.7,
              height: boardHeight*0.3,
              color: Colors.white.withOpacity(0.7),
              child: Column(
                children: [
                  Expanded(
                    child: Column(
                      children: [
                        Expanded(child: SizedBox()),
                        Text(
                          chickenDinner==1?"Black Win!":"White Win!"
                        ),
                      ],
                    ),
                  ),Expanded(
                    child: Column(
                      children: [
                        Expanded(child: SizedBox()),
                        ElevatedButton(
                          onPressed: (){
                            setState((){
                              chickenDinner=0;
                              currentPlayer=1;
                              checkBoard = checkBoard = List.generate(kan, (i) => List.generate(kan,(j)=>0), growable: false);
                            });
                          },
                          child: Text("Reset Game"),
                        ),
                        SizedBox(height: 20,)
                      ],
                    ),
                  ),

                ],
              ),
            ):SizedBox()
          ],
        ),
      ),
       // This trailing comma makes auto-formatting nicer for build methods.
    );
  }


  void putPiece(Offset tapPos,BuildContext context) async {
    final usableHeight = boardHeight * (1-blankPortion*2);
    final usableWidth = boardWidth * (1-blankPortion*2);
    final unitWidth = usableWidth / (kan-1);
    final unitHeight = usableHeight / (kan-1);
    int x = (  (tapPos.dx-(boardWidth*blankPortion)+unitWidth/2) / unitWidth).toInt();
    int y = (  (tapPos.dy-(boardHeight*blankPortion)+unitHeight/2) / unitHeight).toInt();
    print("$x $y");
    //lastStateJson : turn 1 or 2,lastPosition [x,y],board,withAI 0or1
    http.Response res;
    if(checkBoard[x][y]==0) {
      checkBoard[x][y] = currentPlayer;
      var dataMap = {
        "turn": currentPlayer,
        "lastPosition": [y, x],
        "board": checkBoard,
        "withAI": 0
      };
      var lastStateJson = json.encode(dataMap);
      var url = Uri.parse("http://15.164.234.29:5000/tellMeWhatTodo");
      res = await http.post(url, body: lastStateJson);

      if (res!.statusCode == 200) {
        final returnMap = json.decode(res.body);
        setState(() {
          currentPlayer == 1 ? currentPlayer = 2 : currentPlayer = 1;
          chickenDinner = returnMap['winner'];
        });

      }
    }


  }
}
