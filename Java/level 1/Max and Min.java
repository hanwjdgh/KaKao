import java.util.*;

public class GetMinMaxString {
    public String getMinMaxString(String str) {
      String[] arr = str.split(" ");
      int[] tem = new int[arr.length];
      for(int a=0; a<arr.length;a++){
      	tem[a] = Integer.parseInt(arr[a]);
      } 
      Arrays.sort(tem);
    	String s="";
      s=tem[0]+" "+tem[arr.length-1];
      return s;
    }

    public static void main(String[] args) {
        String str = "1 2 3 4";
        GetMinMaxString minMax = new GetMinMaxString();
        //�Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
        System.out.println("�ִ밪�� �ּҰ���?" + minMax.getMinMaxString(str));
    }
}