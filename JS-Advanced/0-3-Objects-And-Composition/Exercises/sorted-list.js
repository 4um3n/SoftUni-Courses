function createSortedList() {
    function _setSize(arr) {
        this.size = arr.length;
    }

    function _checkIndex(index, arr) {
        return (index >= 0 && index < arr.length);
    }

    function _sortNumbers(arr) {
        arr.sort((a, b) => a - b);
    }

    function add(number) {
        this.numbers.push(number);
        this._setSize(this.numbers);
        this._sortNumbers(this.numbers);
    }

    function remove(index) {
        if (this._checkIndex(index, this.numbers)) {
            this.numbers.splice(index, 1);
            this._setSize(this.numbers);
            this._sortNumbers(this.numbers);
        }
    }

    function get(index) {
        if (this._checkIndex(index, this.numbers)) {
            return this.numbers[index];
        }
    }

    return {
        'numbers': [],
        'size': 0,
        '_setSize': _setSize,
        '_checkIndex': _checkIndex,
        '_sortNumbers': _sortNumbers,
        'add': add,
        'remove': remove,
        'get': get
    };
}
