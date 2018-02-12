function waterMelon(n){
  var result = ""
  //함수를 완성하세요
	var arr = "수";
  var arr2 = "박";
  var answer="";
  for(var a=0; a<n;a++){
    if(a%2==0)
      answer+=arr;
    else
      answer+=arr2;
  }
		return answer;
}

// 실행을 위한 테스트코드입니다.
console.log("n이 3인 경우: "+ waterMelon(3))
console.log("n이 4인 경우: "+ waterMelon(4))