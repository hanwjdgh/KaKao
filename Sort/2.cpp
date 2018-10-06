#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(string s1, string s2){
    if(s1+s2 > s2+s1)
        return true;
    else
        return false;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector <string> v;
    
    for(int i=0; i<numbers.size(); i++)
        v.push_back(to_string(numbers[i]));
    sort(v.begin(),v.end(),cmp);
    for(int i=0; i<v.size(); i++)
        answer+=v[i];
    if(answer[0]=='0')
        return "0";
    return answer;
}