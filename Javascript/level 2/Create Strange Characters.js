function toWeirdCase(s){
  var result = ""
  //�Լ��� �ϼ����ּ���
  var list = s.split(" ");
  for(var a=0;a<list.length;a++){
    var tem =list[a].split("");
  	for(var b=0; b<tem.length;b++){
     	if(b%2==1)
        result+=tem[b].toLowerCase();
   		else
        result+=tem[b].toUpperCase();
    }
    if(a<list.length-1)
    	result+=" ";
  }
  return result;
}


// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log("��� : " + toWeirdCase("try hello world"));
