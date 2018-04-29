import java.util.Arrays;
import java.util.Comparator;

class TryHelloWorld
{
    public int chooseCity(int n, int [][]city)
    {
      long sum = 0, half = 0;
      int answer=0, i;
      Arrays.sort(city, new Comparator<int[]>() {
        @Override
        public int compare(int[] start, int[] end) {
          return Integer.compare(start[0], end[0]);
        }
      });
      for (i = 0; i < n; i++)
        sum += city[i][1];
        half = sum / 2;
      if(half*2 != sum) 
        half++; 
  
      sum=0;
  		for (i = 0; i < n; i++){
    		sum += city[i][1];
        if (sum >= half) 
          break;
      }
      return city[i][0];
    }
  
    public static void main(String[] args)
    {
        TryHelloWorld test = new TryHelloWorld();
        int tn = 3;
        int [][]tcity = {{1,100},{10,98},{9,99}};
        System.out.println(test.chooseCity(tn,tcity));
    }
}