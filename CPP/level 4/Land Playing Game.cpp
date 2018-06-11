#include<iostream>
#include<vector>
using namespace std;

int hopscotch(vector<vector<int> > board)
{
	// 함수를 완성하세요.
	int answer = 0;
	vector<int> accum(board[0].size(),0);
  vector<int> tmp(board[0].size(),0);
	int max = 0;
  
  for(int i=0; i<board.size(); i++){
    tmp = accum;
    for(int j=0; j<board[0].size(); j++){
      max = 0;
      for(int k=0; k<board[0].size(); k++){
        if(k!=j){
      		max = (max < tmp[k]) ? tmp[k] : max;
      	}
      }
      accum[j] = board[i][j] + max;
    }
  }
  max = 0;
  for(int i=0; i<accum.size(); i++){
  	max = (max < accum[i]) ? accum[i] : max;
  }
	return max;
}

int main()
{
	vector<vector<int> > test{{1,2,3,5},{5,6,7,8},{4,3,2,1}};
 //아래는 테스트로 출력해 보기 위한 코드입니다.
	cout << hopscotch(test);
}
