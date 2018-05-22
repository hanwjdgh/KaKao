import java.util.Arrays;

class Hanoi {
    int[][] answer;
    int chk=0;
    public void move(int n, int a, int b, int c){
        if(n==1){       
            answer[chk][0] = a;
            answer[chk][1] = c;
            chk++;
        }
        else{
            move(n-1,a,c,b);
            answer[chk][0] = a;
            answer[chk][1] = c;
            chk++;
            move(n-1,b,a,c);
        }
    }
	public int[][] hanoi(int n) {
		// 2차원 배열을 완성해 주세요.
        int num = (int)Math.pow(2,n)-1;
		answer = new int[num][];
        for(int i=0; i< num; i++)
            answer[i] = new int[2];
        move(n,1,2,3);
		return answer;
	}

	// 아래는 테스트로 출력해 보기 위한 코드입니다.
	public static void main(String[] args) {
		Hanoi h = new Hanoi();
		System.out.println(Arrays.toString(h.hanoi(2)));
	}
}
