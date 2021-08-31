function salary(input) {
    let tabsCount = Number(input.shift());
    let salary = Number(input.shift());
    for (let i = 0; i < input.length; i++) {
        let site = input[i];
        if (site == "Facebook") {
            salary -= 150;
        } else if (site == "Instagram") {
            salary -= 100;
        } else if (site == "Reddit") {
            salary -= 50
        }

        if (salary <= 0) {
            console.log("You have lost your salary.");
            return;
        }
    }
    console.log(`${salary.toFixed(0)}`);
}


salary(["10", "750", "Facebook", "Dev.bg", "Instagram", "Facebook", "Reddit", "Facebook", "Facebook"])
salary(["3", "500", "Github.com", "Stackoverflow.com", "softuni.bg"])
