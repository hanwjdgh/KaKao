function waterMelon(n){
  var result = ""
  //�Լ��� �ϼ��ϼ���
	var arr = "��";
  var arr2 = "��";
  var answer="";
  for(var a=0; a<n;a++){
    if(a%2==0)
      answer+=arr;
    else
      answer+=arr2;
  }
		return answer;
}

// ������ ���� �׽�Ʈ�ڵ��Դϴ�.
console.log("n�� 3�� ���: "+ waterMelon(3))
console.log("n�� 4�� ���: "+ waterMelon(4))