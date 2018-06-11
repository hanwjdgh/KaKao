#include<iostream>
using namespace std;

int numOfPrime(int n)
{
	int answer = 0;
  int cnt=0;
	for(int a=2;a<=n;a++){
    cnt=0;
  	for(int b=1;b<=a;b++){
    		if(a%b==0)
          cnt++;
    }
    if(cnt==2)
      answer++;
  }
	return answer;
}

int main()
{
	int testCase = 10;
	int testAnswer = numOfPrime(testCase);

	cout<<testAnswer;
}
