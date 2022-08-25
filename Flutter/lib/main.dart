import 'package:SWGOMOKUGO/constant.dart';
import 'package:SWGOMOKUGO/painter/board.dart';
import 'package:SWGOMOKUGO/painter/piece.dart';
import 'package:flutter/material.dart';

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
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.indigo,
      ),
      home: const MyHomePage(title: 'SW GOMOKUGO'),
      debugShowCheckedModeBanner: false,
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  var checkBoard = List.generate(kan, (i) => List.generate(kan,(j)=>0), growable: false);
  var currentPlayer = 1;
  var chickenDinner =0;
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
                size: Size(500, 500),
                painter : Board(),
                child: CustomPaint(
                  size: Size(500,500),
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


  void putPiece(Offset tapPos,BuildContext context){
    final usableHeight = boardHeight * (1-blankPortion*2);
    final usableWidth = boardWidth * (1-blankPortion*2);
    final unitWidth = usableWidth / (kan-1);
    final unitHeight = usableHeight / (kan-1);
    int x = (  (tapPos.dx-(boardWidth*blankPortion)+unitWidth/2) / unitWidth).toInt();
    int y = (  (tapPos.dy-(boardHeight*blankPortion)+unitHeight/2) / unitHeight).toInt();
    print("$x $y");
    if(checkBoard[x][y]==0) {
      setState(() {
        checkBoard[x][y] = currentPlayer;
        currentPlayer == 1 ? currentPlayer = 2 : currentPlayer = 1;
      });
    }

    if(true){
      setState((){
        chickenDinner=1;
      });
    }
  }
}
//test comment