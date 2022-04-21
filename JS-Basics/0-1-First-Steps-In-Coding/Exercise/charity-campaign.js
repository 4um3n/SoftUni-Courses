function charityCampaign(input) {
    let campaignDaysCount = Number(input[0]);
    let confectionersCount = Number(input[1]);
    let cakesCount = Number(input[2]);
    let wafflesCount = Number(input[3]);
    let pancakesCount = Number(input[4]);
    let incomePerDay = confectionersCount * (cakesCount * 45 + wafflesCount * 5.80 + pancakesCount * 3.20);
    let income = incomePerDay * campaignDaysCount;
    income -= income / 8;
    console.log(income);
}

charityCampaign(["23", "8", "14", "30", "16"]);
charityCampaign(["131", "5", "9", "33", "46"]);