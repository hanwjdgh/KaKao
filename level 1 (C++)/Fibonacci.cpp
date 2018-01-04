#include<iostream>
using namespace std;

long long fibonacci(int n)
{
     long answer = 0;
     long a = 0;
     long b = 1;
     for(int i=0; i<n; i++) {
          if(i != 0){
              answer = a + b;
              a = b;
              b = answer;
          }
      }
      return answer;
}


int main()
{
	int testCase = 10;
	long long testAnswer = fibonacci(testCase);
	cout<<testAnswer;
}