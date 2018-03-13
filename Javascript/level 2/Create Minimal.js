function getMinSum(A,B){
	var answer = 0;
  A.sort(function(a, b) { 
    return a - b;
	});
  B.sort(function(a, b) { 
    return a - b;
	});
  B.reverse();
  for(var i=0; i<A.length;i++)
  	answer+=A[i]*B[i];
	return answer;
}

//아래 코드는 테스트를 위한 출력 코드 입니다.
var tA = [1,2],
	tB = [3,4];

console.log(getMinSum(tA,tB));