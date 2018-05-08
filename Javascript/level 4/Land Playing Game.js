function hopscotch(board, size) {
	var result = 0;
	var max = 0;
  var accum = new Array(board[0].length);
	var tmp = new Array(board[0].length);
  
  for(var i=0; i<board.length; i++){
    for(var j=0; j<board[0].length; j++)
      tmp[j] = accum[j]

    for(var j=0; j<board[0].length; j++){
      accum[j] = board[i][j]+Math.max.apply(null,(tmp.slice(0,j).concat(tmp.slice(j+1,board[0].length))));
    }
  }
	return Math.max.apply(null,accum);
}

 //아래는 테스트로 출력해 보기 위한 코드입니다.
var board = [[ 1, 2, 3, 5 ], [ 5, 6, 7, 8 ], [ 4, 3, 2, 1]];
console.log(hopscotch(board, 3));