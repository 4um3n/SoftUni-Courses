function solve(data) {
    const processor = {
        result: [],
        add(str) {this.result.push(str);},
        remove(str) {this.result = this.result.filter(el => el !== str)},
        print() {console.log(this.result.join(','))}
    };

    function processData() {
        for (const command of data) {
            let [func, val] = command.split(' ');
            processor[func](val);
        }
    }

    processData();
}


solve(['add hello', 'add again', 'remove hello', 'add again', 'print']);
solve(['add pesho', 'add george', 'add peter', 'remove peter','print']);
