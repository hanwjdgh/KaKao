class NLCM {
  public long gcd(long a, long b){
	if(b == 0) 
    return a; 
  return gcd(b, a%b);
	}

	public long lcm(long a,long b){
    return a * b / gcd(a, b);
	}
	public long nlcm(int[] num) {
	long answer = 0;
  long tem=0;
  for(int a=0;a<num.length; a++){
    if(a==0)
    	tem = lcm(num[a],num[a+1]);
    else
      tem = lcm(num[a],tem);
  }
	return tem;
	}
  
	public static void main(String[] args) {
		NLCM c = new NLCM();
		int[] ex = { 2, 6, 8, 14 };
		// 아래는 테스트로 출력해 보기 위한 코드입니다.
		System.out.println(c.nlcm(ex));
	}
}