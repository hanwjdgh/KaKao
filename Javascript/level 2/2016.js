function getDayName(a,b){
	var answer = "";
	var mon = [31,29,31,30,31,30,31,31,30,31,30,31];
  var day=["FRI","SAT","SUN","MON","TUE","WED","THU"];
  var answer= "";
	var sum=0;
  
  for(var i=0; i<a-1; i++){
    sum+=mon[i];
  }
  sum += b;
  answer=day[((sum-1)%7)];
	return answer;
}

//�Ʒ� �ڵ�� �׽�Ʈ�� ���� �ڵ��Դϴ�.
console.log(getDayName(11,3));