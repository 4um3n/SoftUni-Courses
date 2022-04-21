function examPreparation(input) {
    let maxBadAppraisals = Number(input.shift()); let problemsCount = 0;
    let i = 0; let averageScore = 0; let badAppraisals = 0; let problem = "";
    while (input[i] != "Enough") {
        problem = input[i]; let appraisal = Number(input[i + 1]);
        if (appraisal <= 4) {
            badAppraisals += 1;
            if (badAppraisals ==  maxBadAppraisals) {
                return `You need a break, ${badAppraisals} poor grades.`;
            }
        } 
        i += 2; problemsCount++; averageScore += appraisal;
    }
    averageScore = averageScore / problemsCount
    return `Average score: ${averageScore.toFixed(2)}\nNumber of problems: ${problemsCount}\nLast problem: ${problem}`;
}


console.log(examPreparation(["3",
"Money",
"6",
"Story",
"4",
"Spring Time",
"5",
"Bus",
"6",
"Enough"]));
console.log(examPreparation(["2",
"Income",
"3",
"Game Info",
"6",
"Best Player",
"4"]));