class Caesar {
	String caesar(String s, int n) {
    String answer = "";
    int temp = 0;
    
    n = n % 26;
    for(int i=0; i<s.length(); i++) {
      char tem = s.charAt(i);
      	if(tem == ' ') {
					answer+=' ';
					continue;
				}
        temp = tem+n;
        if((tem >= 'a') && (tem <='z')) {
            if(temp > 'z') 
              temp -= 26;
        }
        else if((tem >= 'A') && (tem <='Z')) {
            if(temp > 'Z')   
              temp -= 26;
        }
        answer+=(char)temp;  
    }  
    return answer;
	}

	public static void main(String[] args) {
		Caesar c = new Caesar();
		System.out.println("s는 'a B z', n은 4인 경우: " + c.caesar("a B z", 4));
	}
}
