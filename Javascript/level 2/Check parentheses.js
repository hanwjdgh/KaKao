function is_pair(s){
   var cnt=0
    for(var i=0;i<s.length;i++){
        if(s[i]=="(")
            cnt+=1;
        else
          if(s[i]==")")
            cnt-=1;
        if(cnt<0)
            return false;
    }
   if (cnt!=0)
      return false;
    return true;
}

// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log( is_pair("(hello)()") )
console.log( is_pair(")(") )