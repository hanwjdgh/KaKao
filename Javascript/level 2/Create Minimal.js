function getMinSum(A,B){
	var answer = 0;
  A.sort(function(a, b) { 
    return a - b;
	});
  B.sort(function(a, b) { 
    return a - b;
	});
  B.reverse();
  for(var i=0; i<A.length;i++)
  	answer+=A[i]*B[i];
	return answer;
}

//�Ʒ� �ڵ�� �׽�Ʈ�� ���� ��� �ڵ� �Դϴ�.
var tA = [1,2],
	tB = [3,4];

console.log(getMinSum(tA,tB));