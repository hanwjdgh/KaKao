#include<iostream>
using namespace std;

int sumDivisor(int n)
{
  int sum=0;
  for(int a=1; a<= n; a++){
			if(n%a==0)
      	sum+=a;
  }
	return sum;
}

int main()
{
	int testCase = 12;
	int testAnswer = sumDivisor(testCase);

	cout<<testAnswer;
}