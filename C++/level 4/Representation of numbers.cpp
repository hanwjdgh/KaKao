#include<iostream>
using namespace std;
int expressions(int testCase)
{
	int answer = 1;
	int tem = 0;
  for(int a=1; a<=testCase/2; a++){
  	tem = a;
    for(int b=a+1; b<=testCase/2+1; b++){
      tem+=b;
    	if(tem==testCase){
        answer++;
      	break;
      }
    }
  }
	return answer;
}

int main()
{
	int testNo = 15;
	int testAnswer = expressions(testNo);
// 아래는 테스트로 출력해 보기 위한 코드입니다.
	cout<<testAnswer;
}
