// Your regex myRegex should match 9 items.
// Your regex myRegex should use the global flag.
// Your regex myRegex should use the case insensitive flag.

let quoteSample = "3 blind mice.";
let myRegex = /[^aeiou0-9]/gi;
let result = quoteSample.match(myRegex);