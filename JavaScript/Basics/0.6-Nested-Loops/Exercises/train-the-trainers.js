function grades(input) {
    let n = Number(input.shift());
    let appraisals = {}; let problemsCount = 0;
    while (input[0] != "Finish") {
        let presentation = input.shift();
        problemsCount++;
        for (let _ = 0; _ < n; _++) {
            let appraisal = Number(input.shift());
            if (!(presentation in appraisals)) {
                appraisals[presentation] = 0;
            }
            appraisals[presentation] += appraisal;
        }
        appraisals[presentation] = appraisals[presentation] / n;
    }
    let total = 0;
    let data = Object.entries(appraisals);
    for (let d in data) {
        let p = data[d][0]; let v = data[d][1];
        total += v;
        console.log(`${p} - ${v.toFixed(2)}.`);
    }
    total = total / problemsCount;
    console.log(`Student's final assessment is ${total.toFixed(2)}.`);
}


grades(["2",
"While-Loop",
"6.00",
"5.50",
"For-Loop",
"5.84",
"5.66",
"Finish"]);
grades(["3",
"Arrays",
"4.53",
"5.23",
"5.00",
"Lists",
"5.83",
"6.00",
"5.42",
"Finish"]);