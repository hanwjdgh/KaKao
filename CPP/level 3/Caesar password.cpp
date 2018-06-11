#include<iostream>
#include<string>
using namespace std;

string caesar(string s, int n)
{
  n = n % 26;
	string answer = "";
  
	for(int a=0; a<s.size(); a++) {
		if(s[a] == ' ') {
			answer+=' ';
			continue;
		}
		unsigned char tmp = s[a] + n;
		if(s[a] >= 'a' && s[a] <= 'z') {
			if (tmp > 'z')
				tmp -= 26;
		}
		else if (s[a] >= 'A' && s[a] <= 'Z') {
			if (tmp > 'Z')
				tmp -= 26;
		}
		answer+=tmp;
	}
	return answer;
}

int main()
{
	string text = "a B z";
	int testNo = 4;

	string testAnswer = caesar(text, testNo);

	cout<<testAnswer;
}