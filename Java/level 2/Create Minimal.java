import java.util.*;
class TryHelloWorld
{
    public int getMinSum(int []A, int []B)
    {
        int answer = 0;
				Arrays.sort(A);
        Arrays.sort(B);
        for(int a=0; a<A.length;a++)
          answer +=(A[a]*B[A.length-1-a]);
        return answer;
    }
    public static void main(String[] args)
    {
        TryHelloWorld test = new TryHelloWorld();
        int []A = {1,2};
        int []B = {3,4};
        System.out.println(test.getMinSum(A,B));
    }
}