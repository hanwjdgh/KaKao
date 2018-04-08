#include<iostream>
#include<vector>
#include <algorithm>
using namespace std;

int noOvertime(int no,vector<int> works)
{
	int answer = 0;
	int cnt=0;
  int max=0, index=0;
  while(cnt<no){
  	for(int a=0; a<works.size(); a++){
  		if(a==0){
      	max = works[a];
      	index = a;
    	}
      if(max < works[a]){
      	max = works[a];
      	index = a;
    	}
  	}
    works[index]-=1;
    cnt++;
  }
  for(int b=0; b<works.size(); b++)
    answer += pow(works[b],2);
	return answer;
}

int main()
{
	vector<int> works{4,3,3};
	int testNo = 4;
	int testAnswer = noOvertime(testNo,works);

	cout<<testAnswer;
}