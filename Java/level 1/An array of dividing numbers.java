import java.util.Arrays;

class Divisible {
	public int[] divisible(int[] array, int divisor) {
		//ret�� array�� ���Ե� ������, divisor�� ������ �������� ���ڸ� ������� ��������.
    int cnt=0;
    for(int a=0;a<array.length;a++){
    	if(array[a]%divisor==0)
      	cnt++;
    }
    int[] ret = new int[cnt];
		cnt=0;
    for(int a=0;a<array.length;a++){
    	if(array[a]%divisor==0)
      	ret[cnt++]=array[a];
    }
    return ret;
	}
	// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
	public static void main(String[] args) {
		Divisible div = new Divisible();
		int[] array = {5, 9, 7, 10};
		System.out.println( Arrays.toString( div.divisible(array, 5) ));
	}
}