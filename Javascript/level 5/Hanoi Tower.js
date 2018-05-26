var answer = [];
function move(n,a,b,c){
    var arr=[];
    if(n==1){
        arr.push(a);
        arr.push(c);
        answer.push(arr);
    }
    else{
        move(n-1,a,c,b);
        arr.push(a);
        arr.push(c);
        answer.push(arr);
        move(n-1,b,a,c);
    }
}
function hanoi(n) {
    answer=[];
    move(n,1,2,3);
	return answer;
	// 2차원 배열을 반환해 주어야 합니다.
}

// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log(hanoi(2));