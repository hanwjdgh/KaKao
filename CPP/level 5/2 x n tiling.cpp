#include<iostream>
#include<vector>
using namespace std;

int tiling(int n)
{
    unsigned int answer = 0;
    vector<unsigned int> arr;
    arr.push_back(1);
    arr.push_back(1);
  
    if(n==1)
        answer = arr[n-1];
    else{
  	    for(int i=2; i<n+1; i++){
    	    arr.push_back((arr[i-2]+arr[i-1])%100000);
        }
        answer = arr[n];
    }
	return answer;
}
int main()
{
	int testn = 110;
	int testAnswer = tiling(testn);

	cout<< testAnswer;
}
