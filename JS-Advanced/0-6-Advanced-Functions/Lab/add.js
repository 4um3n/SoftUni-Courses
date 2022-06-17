function solution(num) {
    num = Number(num);

    function sum(n) {
        n = Number(n);
        return num + n;
    }

    return sum;
}
