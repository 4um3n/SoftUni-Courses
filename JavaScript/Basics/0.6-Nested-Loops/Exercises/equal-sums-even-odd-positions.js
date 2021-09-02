function equalSums(input) {
    let start = Number(input[0]);
    let end = Number(input[1]);
    let equals = [];
    for (let n = start; n <= end; n++) {
        n = `${n}`; let evens = 0; let odds = 0;
        for (let i = 0; i < n.length; i++) {
            if (i % 2 == 0) {evens += Number(n[i]);}
            else {odds += Number(n[i]);}
        }
        if (evens == odds) {
            equals.push(n);
        }
    }
    console.log(equals.join(' '));
}


equalSums(["100000", "100050"]);
equalSums(["123456", "124000"]);
equalSums(["299900", "300000"]);
equalSums(["100115", "100120"]);