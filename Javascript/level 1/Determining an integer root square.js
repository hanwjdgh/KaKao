function nextSqaure(n){
  var result = 0;
  //�Լ��� �ϼ��ϼ���
  var tem = Math.sqrt(n);
    if(parseInt(tem) == tem)
        return parseInt(Math.pow(tem+1,2))
    return 'no'
}

// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log("��� : " + nextSqaure(121));