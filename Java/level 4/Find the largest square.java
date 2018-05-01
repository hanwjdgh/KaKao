class TryHelloWorld
{
    public int findLargestSquare(char [][]board)
    {
      	int[][] tem = new int[board.length][board[0].length];
      	int answer = 0;
      	for(int a=0; a<tem.length; a++){
        	for(int b=0; b<tem[0].length; b++)
            tem[a][b] = (board[a][b] == 'X') ? 0 : 1 ; 
        }
      	for(int a = 1; a<board.length; a++){
          for(int b = 1; b<board[0].length; b++){
            if(tem[a][b] == 1){    
              tem[a][b] = Math.min(tem[a-1][b], Math.min(tem[a][b-1], tem[a-1][b-1]))+1;
              answer = answer > tem[a][b] ? answer : tem[a][b];                     
            }
          }
        }
      return (int)Math.pow(answer,2);
    }
    public static void main(String[] args)
    {
        TryHelloWorld test = new TryHelloWorld();
				char [][]board ={
				{'X','O','O','O','X'},
				{'X','O','O','O','O'},
				{'X','X','O','O','O'},
				{'X','X','O','O','O'},
				{'X','X','X','X','X'}};

        System.out.println(test.findLargestSquare(board));
    }
}