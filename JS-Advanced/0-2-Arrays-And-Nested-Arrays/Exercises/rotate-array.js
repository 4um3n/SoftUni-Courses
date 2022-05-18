function rotateArray(arr, n) {
    while (n > 0) {
        arr.unshift(arr.pop());
        n--;
    }

    console.log(arr.join(' '));
}


rotateArray(['1', '2', '3', '4'], 2);
rotateArray(['Banana', 'Orange', 'Coconut', 'Apple'], 15);
