#include<vector>
#include<iostream>
using namespace std;
int gcd(int p, int q){
  if(q==0) return p;
   return gcd(q,p%q);
}
vector<int> gcdlcm(int a,int b)
{
	vector<int> answer;
	answer.push_back(gcd(a,b));
  answer.push_back(a*b/answer[0]);
	return answer;
}
int main()
{
	int a=3, b=12;
	vector<int> testAnswer = gcdlcm(a,b);

	cout<<testAnswer[0]<<" "<<testAnswer[1];
}