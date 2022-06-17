function sortArray(arr, order) {
    function swap(arr, x, y) {
        const temp = arr[x];
        arr[x] = arr[y];
        arr[y] = temp;
    }

    function swapByOrder() {
        return {
            asc(arr, x, y) {
                if (arr[x] > arr[y]) swap(arr, x, y);
            },
            desc(arr, x, y) {
                if (arr[x] < arr[y]) swap(arr, x, y);
            }
        };
    }

    function bubbleSort(arr, order) {
        for (let x = 0; x < arr.length; x++) {
            for (let y = 0; y < arr.length - 1 - x; y++) {
                swapByOrder()[order](arr, y, y + 1);
            }
        }
        return arr;
    }

    return bubbleSort(arr, order);
}


console.log(sortArray([14, 7, 17, 6, 8], 'asc'));
console.log(sortArray([14, 7, 17, 6, 8], 'desc'));