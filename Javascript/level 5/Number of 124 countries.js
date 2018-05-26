function change124(n) {
	var answer = "";
  var arr = "412";
  var a;
  while(parseInt(n) > 0){
    a = parseInt(n%3);
    n = parseInt(n/3);
    if (a==0)
      n -= 1;
    answer = arr[a]+answer;
  }
	return answer;
}

// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log(change124(10));