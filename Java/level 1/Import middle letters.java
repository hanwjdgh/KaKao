class StringExercise{
    String getMiddle(String word){
			String answer="";
      int len = word.length();
      if(len%2==1){
      	answer = word.substring(len/2,len/2+1);
      }
      else
        answer = word.substring(len/2-1,len/2+1);
    	return answer;    
    }
    // �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
    public static void  main(String[] args){
        StringExercise se = new StringExercise();
        System.out.println(se.getMiddle("power"));
    }
}