function rangeOfNumbers(startNum, endNum) {
    if (endNum === startNum) {
        return [startNum]
    } else {
        let arr = rangeOfNumbers(startNum, endNum - 1);
        arr.push(endNum);
        return arr;
    }
};