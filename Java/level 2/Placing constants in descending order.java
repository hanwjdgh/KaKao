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
  
	// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
	public static void  main(String[] args){
		ReverseInt ri = new ReverseInt();
		System.out.println(ri.reverseInt(118372));
	}
}