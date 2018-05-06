class Hopscotch {
    int hopscotch(int[][] board, int size) {
      int result = 0;
      int max = 0;
      int[] accum = new int[board[0].length];
      int[] tmp = new int[board[0].length];
      
      for(int i=0; i<board.length; i++){
       	for(int j=0; j<board[0].length; j++)   
          tmp[j] = accum[j];
       	
				for(int j=0; j<board[0].length; j++){        
        	max = 0;
      		for(int k=0; k<board[0].length; k++){
        		if(k!=j){
      				max = (max < tmp[k]) ? tmp[k] : max;
            }
          }   
          accum[j] = board[i][j] + max;
        }
  		}
      max = 0;
      for(int j=0; j<accum.length; j++)   
				max = (max < accum[j]) ? accum[j] : max;
      return max;
    }

    public static void main(String[] args) {
        Hopscotch c = new Hopscotch();
        int[][] test = { { 1, 2, 3, 5 }, { 5, 6, 7, 8 }, { 4, 3, 2, 1 } };
        //아래는 테스트로 출력해 보기 위한 코드입니다.
        System.out.println(c.hopscotch(test, 3));
    }

}