function joinArray(arr, n) {
    arr = arr.filter((_, i) => i % n === 0);
    return arr;
}


console.log(joinArray(['5', '20', '31', '4', '20'], 2));
console.log(joinArray(['dsa', 'asd', 'test', 'tset'], 2));
console.log(joinArray(['1', '2', '3', '4', '5'], 6));
