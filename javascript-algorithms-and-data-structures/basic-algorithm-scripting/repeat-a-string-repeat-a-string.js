function repeatStringNumTimes(str, num) {
    if (num > 0) {
        let newString = '';
        while (num > 0) {
            newString += str;
            num--;
        }
        return newString
    } else {
        return ''
    }
}

repeatStringNumTimes("abc", 3);