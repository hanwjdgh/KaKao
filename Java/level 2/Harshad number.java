public class HarshadNumber{
	public boolean isHarshad(int num){
		String tem = Integer.toString(num);
    String[] arr = tem.split("");
    int nanu=0;
    for(int a=0; a<arr.length;a++){
    	nanu+=Integer.parseInt(arr[a]);
    }
		return (num%nanu==0)?true:false;
	}
  
       // �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
	public static void  main(String[] args){
		HarshadNumber sn = new HarshadNumber();
		System.out.println(sn.isHarshad(18));
	}
}