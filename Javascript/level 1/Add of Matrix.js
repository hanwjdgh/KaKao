function sumMatrix(A,B){
  for(var a in A){
      for(var b in A[a]){
      	A[a][b]+=B[a][b];
      }
  }
  return A 
}

// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]])) 