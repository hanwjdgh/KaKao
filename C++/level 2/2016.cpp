#include<iostream>
#include<string>
using namespace std;

string getDayName(int a,int b)
{
	int mon[12] = {31,29,31,30,31,30,31,31,30,31,30,31};
  string day[7]={"FRI","SAT","SUN","MON","TUE","WED","THU"};
  string answer= "";
	int sum=0;
  
  for(int i=0; i<a-1; i++){
    sum+=mon[i];
  }
  sum += b;
  answer=day[(sum%7)-1];
	return answer;
}
int main()
{
	int a=5,b=24;

	//아래는 테스트 출력을 위한 코드입니다.
	cout<<getDayName(a,b);
}
