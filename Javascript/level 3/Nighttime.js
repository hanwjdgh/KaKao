function noOvertime(no, works) {
	// 야근 지수를 최소화 하였을 때의 야근 지수는 몇일까요?
  var tem = 0;
	for(var i =0; i<no; i++){
    works[works.indexOf(Math.max.apply(null,works))] -= 1;
  }
	return works.reduce((result,x)=>result+Math.pow(x,2),0);
}