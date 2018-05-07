function findLargestSquare(board)
{
	var answer = 0;
  var tem = new Array(new Array(board.length), new Array(board[0].length));
  var a=0,b=0;
  for(a=0; a<board.length; a++){
    for(b=0; b<board[0].length; b++)
      board[a][b] = (board[a][b] == 'X') ? 0 : 1 ; 
  }
  for(a = 1; a<board.length; a++){
    for(b = 1; b<board[0].length; b++){
      if(board[a][b] == 1){    
        board[a][b] = Math.min(board[a-1][b], Math.min(board[a][b-1], board[a-1][b-1]))+1;
        answer = answer > board[a][b] ? answer : board[a][b];                     
      }
    }
  }
	return Math.pow(answer,2);
}

//아래 코드는 테스트를 위한 출력 코드 입니다.
var testBoard = [['X','O','O','O','X'],['X','O','O','O','O'],['X','X','O','O','O'],['X','X','O','O','O'],['X','X','X','X','X']];
console.log(findLargestSquare(testBoard));