public class Expressions {

	public int expressions(int num) {
		int answer = 1;
		int tem = 0;
  	for(int a=1; a<=num/2; a++){
  		tem = a;
    	for(int b=a+1; b<=num/2+1; b++){
      	tem+=b;
    		if(tem==num){
        	answer++;
      		break;
      	}
    	}
  	}
	return answer;
	}

	public static void main(String args[]) {
		Expressions expressions = new Expressions();
		// 아래는 테스트로 출력해 보기 위한 코드입니다.
		System.out.println(expressions.expressions(15));
	}
}