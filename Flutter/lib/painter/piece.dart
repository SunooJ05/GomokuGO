import 'package:flutter/material.dart';
import 'package:SWGOMOKUGO/constant.dart';
class Piece extends CustomPainter{

  List<List<int>> checkBoard;

  Piece(this.checkBoard);

  @override
  void paint(Canvas canvas, Size size) {
    final Offset startingPoint = Offset(size.width*blankPortion,size.height*blankPortion);
    final usableSize = Size(size.width-startingPoint.dx*2,size.height-startingPoint.dy*2);
    final unitWidth = usableSize.width / (kan-1);
    final unitHeight = usableSize.height / (kan-1);

    int row = checkBoard.length;
    int col = checkBoard[0].length;
    for(var i = 0; i<row;i++){
      for(var j = 0; j<col;j++){
        if(checkBoard[i][j]!=0){
          canvas.drawCircle(startingPoint+Offset(unitWidth*i,unitHeight*j), unitWidth*0.5, Paint()..color=(checkBoard[i][j]==1?Colors.black:Colors.white));
        }
      }
    }
  }

  @override
  bool shouldRepaint(CustomPainter oldDelegate) => true;
  @override
  bool shouldRebuildSemantics(CustomPainter oldDelegate) => true;
}

