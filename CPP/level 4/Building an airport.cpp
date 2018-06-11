#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int chooseCity(int n, vector<pair<int,int>> city)
{
  long long sum = 0, half=0;
  int answer=0, i;
  sort(city.begin(), city.end());

  for (i = 0; i < n; i++)
    sum += city[i].second;

  half = sum / 2;
  if(half*2 != sum) 
    half++; 
  
  for (i = 0, sum = 0; i < n; i++){
    sum += city[i].second;
    if (sum >= half) 
      break;
  }
  return city[i].first;     
}
int main()
{
	int tn = 3;
	pair<int,int> a,b,c;
	a.first = 1, a.second = 100;
	b.first = 10, b.second = 98;
	c.first = 9, c.second = 99;
	vector<pair<int,int>> tcity{a,b,c};

	//�Ʒ��� �׽�Ʈ ����� ���� �ڵ��Դϴ�.
	cout<<chooseCity(tn,tcity);
}
