function squareOfStars (size= 5) {
    for (let _ = 0; _ < size; _++) {
        console.log('* '.repeat(size).trim());
    }
}

squareOfStars();
squareOfStars(5);
squareOfStars(-1);
