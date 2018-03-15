function productMatrix(A, B) {
  var len = A.length;
	var len2 = A[0].length;
	var len3 = B[0].length;
	var answer = Array(len);
	for (var i = 0; i < len; i++) {
		answer[i] = Array(len3).fill(0);
		for (var j = 0; j < len3; j++) {
			for (var k = 0; k < len2; k++) {
				answer[i][j] += A[i][k] * B[k][j];
			}
		}
	}
	return answer;
}

// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
var a = [ [1,2],[4,5] ];
var b = [ [1,2],[4,5] ];
console.log("��� : " + productMatrix(a, b));