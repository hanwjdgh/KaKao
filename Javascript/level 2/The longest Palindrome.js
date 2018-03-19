function longest_palindrom(s){
  var result = 0;
  // 함수를 완성하세요
  for(var i=0;i<s.length;i++){
		for(var a=1; a<=s.length; a++){
  		if(s.substring(i,a)==s.substring(i,a).split("").reverse().join("")){
     	 if(result==0)
       	 result = s.substring(i,a).length;
     	 if(result < s.substring(i,a).length)
        	result = s.substring(i,a).length;
    	}
  	}
  }
  return result;
}


// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log( longest_palindrom("토마토맛토마토") )
console.log( longest_palindrom("토마토맛있어") )
console.log( longest_palindrom("나에게소주만병만주소.") )