import java.util.Arrays;
import java.util.ArrayList;
class LineCombination {
    public long factorial(int n){
        long a = 1;
        for(int i=1; i<=n; i++)
            a *= (long)i;
        return a;
    }
	public int[] setAlign(int n, long k) {
		int[] answer = new int[n];
        ArrayList<Integer> numbers = new ArrayList<>();
        long fac=0;
        int len = n,cnt=0,idx = 1;
        for(int i=1; i<n+1; i++)
            numbers.add(i);
        
        for(int i=0; i<len; i++){
            fac = factorial(n-1);
            if((k-1) == -1)
                idx = n-1; 
            else
                idx = (int)((k-1) / fac);
            answer[cnt++] = numbers.remove(idx);       
            n -=1;
            k %= fac; 
        }
		return answer;
	}

	// 아래는 테스트로 출력해 보기 위한 코드입니다.
	public static void main(String[] args) {
		LineCombination lc = new LineCombination();
		System.out.println(Arrays.toString(lc.setAlign(5,24)));
    }
}