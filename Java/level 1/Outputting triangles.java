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

	// 아래는 테스트로 출력해 보기 위한 코드입니다.
	public static void main(String[] args) {
		PrintTriangle pt = new PrintTriangle();
		System.out.println( pt.printTriangle(8) );
	}
}