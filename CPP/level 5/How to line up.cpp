#include<iostream>
#include<vector>
#include<cstring>
using namespace std;

int factorial(int n){
    int a = 1;
    for(int i=1; i<=n; i++)
        a *= i;
    return a;
}
vector<int> setAlign(int n, long long cnt)
{
	vector<int> answer;
    char arr[n];
    int fac=0,len = n;
    int idx = 1;
    for(int i=1; i<n+1; i++)
        arr[i-1] = i+48;
 
    for(int i=1; i<len+1; i++){
        fac = factorial(n-1);
        idx = (cnt-1) / fac;
        if(idx == -1)
            idx = n-1; 
        answer.push_back(arr[idx]-48);       
        memmove(arr+idx,arr+idx+1,strlen(arr)-idx);
        n -=1;
        cnt %= fac; 
    }
	return answer;
}
int main()
{
	int testn = 3;
	long long testcnt = 5;
	vector<int> testAnswer = setAlign(testn,testcnt);
	// 아래는 테스트로 출력해 보기 위한 코드입니다.

	for(int i=0; i< testAnswer.size(); i++)
	{
		cout << testAnswer[i] << " ";
	}
}
