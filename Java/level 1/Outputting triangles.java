public class PrintTriangle {
	public String printTriangle(int num){
    String arr="";
    String s = "*";
    for(int a=0;a<num;a++){
     	 arr+=s+"\n";
         s+="*";
    }
		return arr;		
	}

	// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
	public static void main(String[] args) {
		PrintTriangle pt = new PrintTriangle();
		System.out.println( pt.printTriangle(8) );
	}
}