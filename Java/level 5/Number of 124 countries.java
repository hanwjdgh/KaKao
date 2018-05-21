class OneTwoFour {
	public String change124(int n) {
		String answer = "";
		String arr = "412";
  	int a;
  	while(n > 0){
  		a = n%3;
    	n /= 3;
      if (a==0)
      	n -= 1;
      answer = arr.charAt(a)+answer;
  	}  
		return answer;
	}

	// 아래는 테스트로 출력해 보기 위한 코드입니다.
	public static void main(String[] args) {
		OneTwoFour oneTwoFour = new OneTwoFour();
		System.out.println(oneTwoFour.change124(10));
	}
}
