#include<vector>
#include<iostream>
#include <algorithm> 
using namespace std;

vector<int> bestSet(int no,int sum)
{
	vector<int> answer(1,-1);
  vector<int> result(no, sum/no);
	if(no > sum)
  	return answer;
  for(int a=0; a<sum%no; a++)
  	result[a%no]+=1;
  sort(result.begin(), result.end());   
	return result;
}
int main()
{
	int n=3, s=13;
	vector<int> test= bestSet(n,s);

// 아래는 테스트로 출력해 보기 위한 코드입니다.
	for(int i=0; i<test.size(); i++)
		cout << test[i] << " ";
}
