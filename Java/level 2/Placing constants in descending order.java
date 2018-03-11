import java.util.*;

public class ReverseInt {
	public int reverseInt(int n){
		String arr = Integer.toString(n);
    String[] tem = arr.split("");
    String answer="";
    Arrays.sort(tem);
    for(int a=tem.length-1; a>-1;a--)
      answer+=tem[a];
		return Integer.parseInt(answer);
	}
  
	// 아래는 테스트로 출력해 보기 위한 코드입니다.
	public static void  main(String[] args){
		ReverseInt ri = new ReverseInt();
		System.out.println(ri.reverseInt(118372));
	}
}