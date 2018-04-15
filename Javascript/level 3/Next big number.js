function nextBigNumber(n){
  var cnt = n.toString(2).match(/1/g).length;
  for (var i = n+1; ; i++) { 
    if ( cnt == i.toString(2).match(/1/g).length) { 
      return i 
    } 
  }
}

//아래 코드는 테스트를 위한 코드입니다.
console.log(nextBigNumber(78));