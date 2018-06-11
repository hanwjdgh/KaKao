#include<iostream>
#include<vector>
using namespace std;
long long gcd(long long a, long long b){
	long long c;
	if(b == 0) 
    return a; 
  return gcd(b, a%b);
}

long long lcm(long long a,long long b){
    return a * b / gcd(a, b);
}

long long nlcm(vector<int> num){
	long long answer = 0;
  long long tem=0;
  for(int a=0;a<num.size(); a++){
    if(a==0)
    	tem = lcm(num[a],num[a+1]);
    else
      tem = lcm(num[a],tem);
  }
	return tem;
}

int main(){
	vector<int> test{2,11,45,54,56,62,64,73,82,84};

	// 아래는 테스트로 출력해 보기 위한 코드입니다.
	cout << nlcm(test);
}
