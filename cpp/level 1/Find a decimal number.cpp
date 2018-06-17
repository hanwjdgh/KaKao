#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    if(n==2)
        return 1;
    for(int i=2;i<n;i++) {
		if(n % i == 0) {
			return 0 + solution(n-1);
			break;
		}
	}
    return 1 + solution(n-1);
}
/**/