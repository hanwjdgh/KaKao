function gcd(a, b){
	if(b == 0) 
    return a; 
  return gcd(b, a%b);
}

function lcm(a,b){
  return a * b / gcd(a, b);
}

function nlcm(num) {
	return num.sort((a, b) => a - b).reduce(lcm);
}


// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log(nlcm([14,2,8,6]));