function bestSet(n, s) {
	var answer = [-1];
  var result = [];
	if(n > s){
  		return answer;
  }
  for(var a=0; a<n; a++)
  		result[a]=parseInt(s/n);
  for(var a=0; a<s%n; a++)
  		result[a%n]+=1;
  result.sort();
  return result;
}

// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log(bestSet(3,13));