// Your regex should use the global flag.
// Your regex should find 6 non-alphanumeric characters in the string The five boxing wizards jump quickly..
// Your regex should use the shorthand character to match characters which are non-alphanumeric.
// Your regex should find 8 non-alphanumeric characters in the string Pack my box with five dozen liquor jugs.
// Your regex should find 6 non-alphanumeric characters in the string How vexingly quick daft zebras jump!
// Your regex should find 12 non-alphanumeric characters in the string 123 456 7890 ABC def GHI jkl MNO pqr STU vwx YZ.

let quoteSample = "The five boxing wizards jump quickly.";
let nonAlphabetRegex = /\W/g;
let result = quoteSample.match(nonAlphabetRegex).length;