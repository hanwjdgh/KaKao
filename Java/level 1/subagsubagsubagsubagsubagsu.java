public class WaterMelon {
	public String watermelon(int n){
		String arr = "��";
    String arr2 = "��";
  	String answer="";
    for(int a=0; a<n;a++){
    	if(a%2==0)
        answer+=arr;
      else
        answer+=arr2;
    }
		return answer;
	}

	// ������ ���� �׽�Ʈ�ڵ��Դϴ�.
	public static void  main(String[] args){
		WaterMelon wm = new WaterMelon();
		System.out.println("n�� 3�� ���: " + wm.watermelon(3));
		System.out.println("n�� 4�� ���: " + wm.watermelon(4));
	}
}