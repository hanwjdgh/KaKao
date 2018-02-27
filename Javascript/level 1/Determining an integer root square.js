function nextSqaure(n){
  var result = 0;
  //함수를 완성하세요
  var tem = Math.sqrt(n);
    if(parseInt(tem) == tem)
        return parseInt(Math.pow(tem+1,2))
    return 'no'
}

// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log("결과 : " + nextSqaure(121));