function adder(a, b){
    var result = 0
    //�Լ��� �ϼ��ϼ���
    var tem;
    if(a>b){
    	tem = a;
      a = b;
      b = tem;
    }
    for(var i=a; i<=b;i++)
      result+=i;
    return result;
}


// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log( adder(3, 5) )