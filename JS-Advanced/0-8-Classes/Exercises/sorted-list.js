class List {
    constructor() {
        this.data = [];
        this.size = this.data.length;
    }

    _setSize() {
        this.size = this.data.length;
    }

    _sortData(type) {
        this.data.sort((a, b) => a - b);
    }

    add(element) {
        this.data.push(element);
        this._sortData();
        this._setSize();
    }

    remove(index) {
        if (index < 0 || index >= this.data.length) {
            throw new Error('Invalid index');
        }

        this.data.splice(index, 1);
        this._setSize();
    }

    get(index) {
        if (index < 0 || index >= this.data.length) {
            throw new Error('Invalid index');
        }

        return this.data[index];
    }
}


let list = new List();
list.add(5);
list.add(6);
list.add(7);
console.log(list.get(1));
list.remove(1);
console.log(list.get(1));
console.log(list.hasOwnProperty('size'));
