function sequence(input) {
    let n = Number(input[0]); let x = 1;
    while (x < n) {
        console.log(x); x = x * 2 + 1;
    }
}


sequence(["3"])
sequence(["8"])
sequence(["17"])
sequence(["31"])