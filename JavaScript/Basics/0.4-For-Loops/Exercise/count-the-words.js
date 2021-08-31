function countTheWords(input) {
    let text = input[0];
    text = text.split(" ");
    if (text.length > 10) {
        console.log(`The message is too long to be send! Has ${text.length} words.`)
    } else {
        console.log(`The message was sent successfully!`)
    }
}


countTheWords(["This message has exactly eleven words. One more as it's allowed!"])
countTheWords((["This message has ten words and you can send it!"]))