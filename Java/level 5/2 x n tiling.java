class TryHelloWorld {
	public int tiling(int n) {
		int answer = 0;
        int a=1, b=1, t=0;
        
        if (n==1)
            answer = a;
        else{
            for(int i=2; i<n+1; i++){
                t = a;
                a = (a+b)%100000;
                b = t%100000;
            }
            answer = a;
        }
		return answer;
	}

	public static void main(String args[]) {
		TryHelloWorld tryHelloWorld = new TryHelloWorld();
		// 아래는 테스트로 출력해 보기 위한 코드입니다.
		System.out.print(tryHelloWorld.tiling(2));
	}
}