function leapYears(input) {
    let leapYear = Number(input[0]); 
    let endYear = Number(input[1]); 
    for (let i = leapYear; i <= endYear; i += 4) {
        console.log(i);
    }
}


leapYears(["1908", "1919"]);
leapYears(["2000", "2011"]);
leapYears(["1548", "1597"]);
leapYears(["2020", "2032"]);