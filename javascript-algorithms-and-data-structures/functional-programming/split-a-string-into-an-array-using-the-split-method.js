function splitify(str) {
    let newStr = str.split(/\W/);

    return newStr;
}

splitify("Hello World,I-am code");