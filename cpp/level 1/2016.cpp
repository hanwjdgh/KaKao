#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    int mon[12] = {31,29,31,30,31,30,31,31,30,31,30,31};
    string day[7]={"FRI","SAT","SUN","MON","TUE","WED","THU"};
    string answer= "";
	int sum=0;
  
    for(int i=0; i<a-1; i++)
        sum+=mon[i];
    sum += b;
    answer=day[((sum-1)%7)];
	return answer;
}