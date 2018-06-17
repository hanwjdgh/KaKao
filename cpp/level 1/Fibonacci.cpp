#include <string>
#include <vector>

using namespace std;

int solution(int n) {
     int answer = 0;
     int a = 0;
     int b = 1;
     for(int i=0; i<n; i++) {
          if(i != 0){
              answer = (a + b)%1234567;
              a = b%1234567;
              b = answer%1234567;
          }
      }
      return answer;
}