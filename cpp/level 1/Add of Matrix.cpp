#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int> >answer;

    int temp=0;
    for(int a=0; a<arr1.size(); a++){
    vector<int> tem;
    for(int b=0; b<arr2[0].size();b++){
      temp=0;
      for(int c=0; c<arr2.size();c++){
        temp+=(arr1[a][c]*arr2[c][b]);
      }
      tem.push_back(temp);
     }
     answer.push_back(tem);
    }
    return answer;
}