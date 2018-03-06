class ProductMatrix {
	public int[][] productMatrix(int[][] A, int[][] B) {
		int[][] answer = new int[A.length][B[0].length];
		for(int a=0;a<A.length;a++){
    	for(int b=0;b<B[0].length;b++){
      	for(int c=0; c<B.length;c++){
          answer[a][b]+=(A[a][c]*B[c][b]);
        }
      }
    }
		return answer;
	}

	public static void main(String[] args) {
		ProductMatrix c = new ProductMatrix();
		int[][] a = { { 1, 2 }, { 2, 3 } };
		int[][] b = { { 3, 4 }, { 5, 6 } };
      // �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
      System.out.println("����� ���� : " + c.productMatrix(a, b));
	}
}
