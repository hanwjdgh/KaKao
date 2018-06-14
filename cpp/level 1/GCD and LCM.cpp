#include <string>
#include <vector>

using namespace std;

int gcd(int p, int q){
  if(q==0) return p;
   return gcd(q,p%q);
}

vector<int> solution(int n, int m) {
    vector<int> answer;
	answer.push_back(gcd(n,m));
    answer.push_back(n*m/answer[0]);
	return answer;
}