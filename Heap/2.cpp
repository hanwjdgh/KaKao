#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int stock, vector<int> dates, vector<int> supplies, int k) {
    int answer = 0;
    priority_queue< int, vector<int>, less<int> > pq;
    
    int s = 0;
    
    while(stock < k){
        for(int i=s; i<dates.size(); i++){
            if(dates[i] <= stock)
                pq.push(supplies[i]);
            else{
                s = i;
                break;
            }
        }
        answer += 1;
        stock += pq.top();
        pq.pop();
    }
    return answer;
}