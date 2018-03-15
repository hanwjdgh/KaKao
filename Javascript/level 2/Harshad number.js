function Harshad(n){
  //함수를 완성하세요
	var tem = n.toString();
  var arr = tem.split("");
  var nanu=0;
  for(var a=0; a<arr.length;a++){
    	nanu+=parseInt(arr[a]);
    }
	return (n%nanu==0)?true:false;
}

// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log(Harshad(18))