function caesar(s, n) {
	var answer = ""
  n = n % 26 
  for ( let i = 0; i < s.length; i++ ) { 
    var word = s.charCodeAt(i) 
    if ( word == 32 ){
      answer +=" "
    	continue
    }
    var tem = word+n
    if ( word >= 97 && word <= 122 ){ 
      if ( tem > 122 )
        tem-=26
    }
    else if ( word >= 65 && word <= 90 ){
      if ( tem > 90 )  {
        tem-=26
      }
    }
    answer += String.fromCharCode(tem)
  } 
  return answer
}

// ������ ���� �׽�Ʈ�ڵ��Դϴ�.
console.log('s�� "a B z", n�� 4�� ���: ' + caesar("wVLREnMjHgsMCQKGmyipVH tanVgQhwIeKHHey cDXlP OyRVM", 42));