#include<iostream>
#include<vector>
using namespace std;

vector<vector<int> >productMatrix(vector<vector<int> >A, vector<vector<int> >B)
{
	vector<vector<int> >answer;

  int temp=0;
	for(int a=0; a<A.size(); a++){
  vector<int> tem;
    for(int b=0; b<B[0].size();b++){
      temp=0;
      for(int c=0; c<B.size();c++){
      	temp+=(A[a][c]*B[c][b]);
      }
      tem.push_back(temp);
    }
     answer.push_back(tem);
  }
	return answer;
}

int main()
{
	vector<vector<int> >A{{1,2},{2,3}};
	vector<vector<int> >B{{2,3},{3,4}};
	vector<vector<int> > testAnswer = productMatrix(A,B);

	for(int i=0;i<testAnswer.size(); i++)
	{
		for(int j=0;j<testAnswer[i].size(); j++)
			cout<<testAnswer[i][j]<<" ";
		cout<<"\n";
	}
}