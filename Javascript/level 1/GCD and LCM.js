function gcdlcm(a, b) {
    var answer = [];
		answer[0] = gcd(a,b);
    answer[1] = (a*b)/answer[0];
    return answer;
}

function gcd(p, q){
    if (q == 0) return p;
    return gcd(q, p%q);
}
// �Ʒ��� �׽�Ʈ�� ����� ���� ���� �ڵ��Դϴ�.
console.log(gcdlcm(3,12));