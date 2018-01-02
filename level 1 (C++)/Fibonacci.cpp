#include<iostream>
using namespace std;

long long fibonacci(int n)
{
  if(n<=1)
    return n;
  else
    return ( fibonacci(n-1) + fibonacci(n-2) );
}


int main()
{
	int testCase = 10;
	long long testAnswer = fibonacci(testCase);

	cout<<testAnswer;
}