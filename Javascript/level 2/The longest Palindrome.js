function longest_palindrom(s){
  var result = 0;
  // �Լ��� �ϼ��ϼ���
  for(var i=0;i<s.length;i++){
		for(var a=1; a<=s.length; a++){
  		if(s.substring(i,a)==s.substring(i,a).split("").reverse().join("")){
     	 if(result==0)
       	 result = s.substring(i,a).length;
     	 if(result < s.substring(i,a).length)
        	result = s.substring(i,a).length;
    	}
  	}
  }
  return result;
}


// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log( longest_palindrom("�丶����丶��") )
console.log( longest_palindrom("�丶����־�") )
console.log( longest_palindrom("�����Լ��ָ������ּ�.") )