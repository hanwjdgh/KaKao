function hide_numbers(s){
  let hide = null; 
  hide = s.substr(0,s.length-4).replace(/\d/g,"*") ;
  s = s.substr(s.length-4,4) ;
  return hide.concat(s);
  // s.replace(/\d(?=\d{4})/g, "*");
}

// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log("결과 : " + hide_numbers('01033334444'));