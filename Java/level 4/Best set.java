import java.util.Arrays; //테스트로 출력해 보기 위한 코드입니다.

public class BestSet {

    public int[] bestSet(int n, int s){
        int[] answer = {-1};
      	int[] result = new int[n];
				if(n > s)
  				return answer;
      	for(int a=0; a<n; a++)
  					result[a]=s/n;
      	for(int a=0; a<s%n; a++)
  					result[a%n]+=1;
      	Arrays.sort(result);
      	return result;
    }
    public static void main(String[] args) {
        BestSet c = new BestSet();
        //아래는 테스트로 출력해 보기 위한 코드입니다.
        System.out.println(Arrays.toString(c.bestSet(3,13)));
    }

}