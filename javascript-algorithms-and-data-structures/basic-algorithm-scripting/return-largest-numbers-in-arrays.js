function largestOfFour(arr) {
    let result = [];

    for (let i = 0; i < arr.length; i++) {
        let maxNumber = arr[i][0];
        for (let y = 1; y < arr[i].length; y++) {
            if (arr[i][y] > maxNumber) {
                maxNumber = arr[i][y];
            }
        }
        result[i] = maxNumber;
    }
    return result;
}

largestOfFour([
    [4, 5, 1, 3],
    [13, 27, 18, 26],
    [32, 35, 37, 39],
    [1000, 1001, 857, 1]
]);