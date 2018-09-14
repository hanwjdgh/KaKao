#include <iostream>
#include <vector>

#define MAX 10000001

using namespace std;

bool prime[MAX];

long long solution(int N) {
    long long answer = 0;
    prime[0] = prime[1] = true;
    
    for(int i=2; i<=N; i++){
        if(prime[i])
            continue;
        answer+=i;
        for(int j=i; j<=N; j+=i){
            if(prime[j])
                continue;
            prime[j] = true;
        }
    }
    return answer;
}