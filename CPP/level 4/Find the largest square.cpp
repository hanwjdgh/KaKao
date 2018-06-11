#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>
using namespace std;

int findLargestSquare(vector<vector<char>> board)
{
  int answer = 0;
  vector<vector<int>> tem(board.size(),vector<int>(board[0].size(),0));

  for(int a = 0; a<board.size(); a++){    
    for(int b = 0; b<board[0].size(); b++){
        tem[a][b] = (board[a][b] == 'X') ? 0 : 1 ; 
    }
  }

  for(int a = 1; a<board.size(); a++){
    for(int b = 1; b<board[0].size(); b++){
      if(tem[a][b] == 1){    
      	tem[a][b] = min(tem[a-1][b], min(tem[a][b-1], tem[a-1][b-1]))+1;
        answer = answer > tem[a][b] ? answer : tem[a][b];                     
      }
    }
  }
  return pow(answer,2);
}

int main()
{
	vector<vector<char>> board{
				{'X','O','O','O','X'},
				{'X','O','O','O','O'},
				{'X','X','O','O','O'},
				{'X','X','O','O','O'},
				{'X','X','X','X','X'}};

	//아래는 테스트 출력을 위한 코드입니다.
	cout<<findLargestSquare(board);
}
