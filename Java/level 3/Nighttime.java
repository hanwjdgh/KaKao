class NoOvertime {
	public int noOvertime(int no, int[] works) {
		int answer = 0;
		int cnt=0;
  	int max=0, index=0;
  	while(cnt<no){
  		for(int a=0; a<works.length; a++){
  			if(a==0){
      		max = works[a];
      		index = a;
    		}
      	if(max < works[a]){
      		max = works[a];
      		index = a;
    		}
  		}
    	works[index]-=1;
    	cnt++;
  	}
 	 	for(int b=0; b<works.length; b++)
    	answer += Math.pow(works[b],2);
		return answer;
	}
	public static void main(String[] args) {
		NoOvertime c = new NoOvertime();
		int []test = {4,3,3};
		System.out.println(c.noOvertime(4,test));
	}
}
