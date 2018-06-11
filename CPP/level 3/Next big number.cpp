#include<iostream>
using namespace std;

int nextBigNumber(int n) {
	int tem=n+1;
	int cnt = 0, tcnt = 0;
	for (int i = 1; n>0; i *= 10) {
		int binary = n % 2;
		if (binary == 1)
			cnt++;
		n /= 2;
	}
	for (int j = tem; ;j++) {
		tcnt = 0;
		int temp = j;
		for (int i = 1; temp>0; i *= 10) {
			int binar = temp % 2;
			if (binar == 1)
				tcnt++;
			temp /= 2;
		}
		
		if (tcnt == cnt)
			return j;
	}
}
int main() {
	int n = 78;
	//아래는 테스트 출력을 위한 코드입니다.
	cout << nextBigNumber(n);
}
