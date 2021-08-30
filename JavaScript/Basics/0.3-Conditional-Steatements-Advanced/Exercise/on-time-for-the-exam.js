function isStudentOnTime(input) {
    let examHour = Number(input[0]);
    let examMinute = Number(input[1]);
    let arriveHour = Number(input[2]);
    let arriveMinute = Number(input[3]);
    let examMinutes = examHour * 60 + examMinute;
    let arriveMinutes = arriveHour * 60 + arriveMinute;
    let diff = Math.abs(arriveMinutes - examMinutes);

    if (arriveMinutes == examMinutes) {
        console.log("On time");
    } else if (arriveMinutes > examMinutes) {
        console.log("Late");
        if (diff < 60) {
            console.log(`${diff} minutes after the start`)
        } else {
            examHour = Math.floor(diff / 60);
            examMinute = diff % 60;
            if (examMinute < 10) {
                examMinute = `0${examMinute}`;
            }
            console.log(`${examHour}:${examMinute} hours after the start`);
        }
    
    } else if (arriveMinutes < examMinutes) {
        if (diff > 59) {
            console.log("Early")
            examHour = Math.floor(diff / 60);
            examMinute = diff % 60;
            if (examMinute < 10) {
                examMinute = `0${examMinute}`;
            }
            console.log(`${examHour}:${examMinute} hours before the start`);
        }else if (diff <= 30) {
            console.log("On time");
            console.log(`${diff} minutes before the start`);
        } else if (diff < 60) {
            console.log("Early");
            console.log(`${diff} minutes before the start`);
        }
    }
}

isStudentOnTime(["9",
"30",
"9",
"50"])
isStudentOnTime(["9",
"00",
"8",
"30"])
isStudentOnTime(["16",
"00",
"15",
"00"])
isStudentOnTime(["9",
"00",
"10",
"30"])
isStudentOnTime(["14",
"00",
"13",
"55"])
isStudentOnTime(["11",
"30",
"8",
"12"])
isStudentOnTime(["11",
"30",
"10",
"55"])
isStudentOnTime(["10",
"00",
"10",
"00"])
