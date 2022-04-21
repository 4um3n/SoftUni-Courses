function projectsCreation(input) {
    let architectName = input[0];
    let projectsCount = Number(input[1]);
    let timeForWork = projectsCount * 3;
    console.log(`The architect ${architectName} will need ${timeForWork} hours to complete ${projectsCount} project/s.`);
}

projectsCreation(["George", "4"]);
