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
        //아래는 테스트로 출력해 보기 위한 코드입니다.
        System.out.println("최대값과 최소값은?" + minMax.getMinMaxString(str));
    }
}