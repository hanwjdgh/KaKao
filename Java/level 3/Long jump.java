class JumpCase {

    public int jumpCase(int num) {
        int answer = 0;
        if(num==1)
          return 1;
        else if(num==2)
          return 2;
        answer = jumpCase(num - 1) + jumpCase(num - 2);
        return answer;
    }

    public static void main(String[] args) {
        JumpCase c = new JumpCase();
        int testCase = 4;
        //�Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
        System.out.println(c.jumpCase(testCase));
    }
}