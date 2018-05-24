function tiling(n) {
	var answer = 0;
    var arr = [1, 1]
    
    if(n==1)
        answer = arr[0];
    else{
        for(var i=2; i<n+1; i++){
            arr.push((arr[i-2]+arr[i-1])%100000);
        }
        answer = arr[n];
    }
	return answer;
}

// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log(tiling(2));