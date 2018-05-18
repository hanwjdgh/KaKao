#include<iostream>
#include<vector>
using namespace std;

vector<vector<int> > answer;
void move(int n, int a, int b, int c){
    vector<int> arr;
    if(n==1){       
        arr.push_back(a);
        arr.push_back(c);
        answer.push_back(arr);
    }
    else{
        move(n-1,a,c,b);
        arr.push_back(a);
        arr.push_back(c);
        answer.push_back(arr);
        move(n-1,b,a,c);
    }
}
vector<vector<int> > hanoi(int no)
{
    move(no,1,2,3);
	return answer;
}
int main()
{
	int testNo = 2;

	vector<vector<int> > testAnswer = hanoi(testNo);

	// 아래는 테스트로 출력해 보기 위한 코드입니다.
	for(int i=0; i< testAnswer.size(); i++)
	{
		for(int j=0; j<testAnswer[i].size(); j++)
		{
			cout << testAnswer[i][j] << " ";
		}
		cout << "\n";
	}
}
