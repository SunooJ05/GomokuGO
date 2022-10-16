import 'package:SWGOMOKUGO/constant.dart';
import 'package:flutter/material.dart';

class Board extends CustomPainter{

  @override
  void paint(Canvas canvas, Size size) {

    final Paint outlinePaint = Paint()..color=Colors.black..strokeWidth=2;
    final Paint inlinePaint = Paint()..color=Colors.black..strokeWidth=1;

    final Offset startingPoint = Offset(size.width*blankPortion,size.height*blankPortion);
    final usableSize = Size(size.width-startingPoint.dx*2,size.height-startingPoint.dy*2);
    final unitWidth = usableSize.width / (kan-1);
    final unitHeight = usableSize.height / (kan-1);

    final Rect rect = Offset.zero & size;

    canvas.drawRect(
      rect,
      Paint()..color = boardColor
    );
    canvas.drawLine(Offset.zero, Offset(0,size.height),outlinePaint);
    canvas.drawLine(Offset.zero, Offset(size.width,0),outlinePaint);
    canvas.drawLine(Offset(0,size.height), Offset(size.width,size.height),outlinePaint);
    canvas.drawLine(Offset(size.width,0), Offset(size.width,size.height),outlinePaint);
    for(var i = 0;i<kan;i++){
      canvas.drawLine(
        Offset(startingPoint.dx+unitWidth*i,startingPoint.dy),
        Offset(startingPoint.dx+unitWidth*i,startingPoint.dy+usableSize.height),
        inlinePaint
      );
    }
    for(var i = 0;i<kan;i++){
      canvas.drawLine(
        Offset(startingPoint.dx,startingPoint.dy+unitHeight*i),
        Offset(startingPoint.dx+usableSize.width,startingPoint.dy+unitHeight*i),
        inlinePaint
      );
    }

    for(var i = 0;i<kan;i++){
      for(var j = 0;j<kan;j++){
        if((i-3)%4==0&&(j-3)%4==0){
          canvas.drawCircle(startingPoint+Offset(unitWidth*i,unitHeight*j), 4, Paint()..color = Colors.black);
        }
      }
    }


  }

  @override
  bool shouldRepaint(CustomPainter oldDelegate) => false;
  @override
  bool shouldRebuildSemantics(CustomPainter oldDelegate) => false;
}

