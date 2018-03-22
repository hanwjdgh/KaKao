function toWeirdCase(s){
  var result = ""
  //함수를 완성해주세요
  var list = s.split(" ");
  for(var a=0;a<list.length;a++){
    var tem =list[a].split("");
  	for(var b=0; b<tem.length;b++){
     	if(b%2==1)
        result+=tem[b].toLowerCase();
   		else
        result+=tem[b].toUpperCase();
    }
    if(a<list.length-1)
    	result+=" ";
  }
  return result;
}


// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log("결과 : " + toWeirdCase("try hello world"));
