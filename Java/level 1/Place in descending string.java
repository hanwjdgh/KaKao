import java.util.*;

public class ReverseStr {
	public String reverseStr(String str){
		String [] arr = str.split("");
		Arrays.sort(arr);
    Collections.reverse(Arrays.asList(arr));
    String s = String.join("",arr);
		return s;
	}

	// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
	public static void main(String[] args) {
		ReverseStr rs = new ReverseStr();
		System.out.println( rs.reverseStr("Zbcdefg") );
	}
}