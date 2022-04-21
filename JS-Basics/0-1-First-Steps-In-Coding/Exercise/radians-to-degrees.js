function convert(input) {
    let rad = Number(input[0]);
    let deg = rad * 180 / Math.PI;
    console.log(deg.toFixed(0));
}

convert(["3.1416"]);
convert(["6.2832"]);
convert(["0.7854"]);
convert(["0.5236"]);
