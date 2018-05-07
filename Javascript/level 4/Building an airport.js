function chooseCity(n,city)
{
  var sum=0, half=0;
	var answer = 0,i;
	city.sort(function(a,b){
  	return a[0]-b[0];
  });
  for (i = 0; i < n; i++)
    sum += city[i][1];
    half = sum / 2;
  if(half*2 != sum) 
    half++; 
  sum=0;
  for (i = 0; i < n; i++){
    sum += city[i][1];
    if (sum >= half) 
      break;
  }
  return city[i][0];
}

//아래 코드는 테스트를 위한 출력 코드 입니다.
var tA = 3,
	tCity = [[1,5],[3,3],[2,2]];

console.log(chooseCity(tA,tCity));