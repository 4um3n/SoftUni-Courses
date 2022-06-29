function solution(arr, start, end) {
    if (!Array.isArray(arr)) {
        return NaN;
    }

    start = (Number(start) < 0) ? 0 : Number(start);
    end = (Number(end) < arr.length) ? Number(end) : arr.length - 1;

    return arr.slice(start, end+1).reduce((a, c) => Number(a) + Number(c));
}


// console.log(solution([10, 20, 30, 40, 50, 60], 3, 300));
console.log(solution([10, 'twenty', 30, 40], 0, 2));