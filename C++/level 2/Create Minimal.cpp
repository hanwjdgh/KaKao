#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int getMinSum(vector<int> A, vector<int> B)
{
	int answer = 0;
	sort(A.begin(), A.end());
  sort(B.begin(), B.end(), greater<int>());
  for(int a=0; a<A.size(); a++){
    cout<<A[a]<<B[a]<<endl;
  	answer += (A[a] * B[a]);
  }
	return answer;
}
int main()
{
	vector<int> tA{1,2}, tB{3,4};

	//�Ʒ��� �׽�Ʈ ����� ���� �ڵ��Դϴ�.
	cout<<getMinSum(tA,tB);
}