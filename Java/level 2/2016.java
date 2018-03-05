class TryHelloWorld
{
    public String getDayName(int a, int b)
    {
        String answer = "";
				int[] mon = {31,29,31,30,31,30,31,31,30,31,30,31};
  			String[] day={"FRI","SAT","SUN","MON","TUE","WED","THU"};
				int sum=0;
  
  			for(int i=0; i<a-1; i++){
    				sum+=mon[i];
  			}
  			sum += b;
 				answer=day[((sum-1)%7)];
        return answer;
    }
    public static void main(String[] args)
    {
        TryHelloWorld test = new TryHelloWorld();
        int a=11, b=3;
        System.out.println(test.getDayName(a,b));
    }
}