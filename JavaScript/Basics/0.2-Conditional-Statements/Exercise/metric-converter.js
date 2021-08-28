function metricConverter(input) {
    let n = Number(input[0]);
    let inData = input[1];
    let outData = input[2];
    if (inData == "mm") {
        n *= 0.001;
    } else if (inData == "cm") {
        n *= 0.01;
    }

    if (outData == "cm") {
        n *= 100;
    } else if (outData == "mm") {
        n *= 1000;
    }

    console.log(n.toFixed(3));
}

metricConverter(["12","mm","m"]);
metricConverter(["150","m","cm"]);
metricConverter(["45","cm","mm"]);
