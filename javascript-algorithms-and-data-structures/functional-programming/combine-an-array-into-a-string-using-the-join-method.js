function sentensify(str) {
    let strSplit = str.split(/\W/);
    let strJoin = strSplit.join(" ");

    return strJoin
}

sentensify("May-the-force-be-with-you");