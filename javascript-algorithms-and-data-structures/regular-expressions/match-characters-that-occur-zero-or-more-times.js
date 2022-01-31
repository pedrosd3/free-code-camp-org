// Your regex chewieRegex should use the * character to match zero or more a characters.
// Your regex should match the string A in chewieQuote.
// Your regex should match the string Aaaaaaaaaaaaaaaa in chewieQuote.
// Your regex chewieRegex should match 16 characters in chewieQuote.
// Your regex should not match any characters in the string He made a fair move. Screaming about it can't help you.
// Your regex should not match any characters in the string Let him have it. It's not wise to upset a Wookiee.

let chewieQuote = "Aaaaaaaaaaaaaaaarrrgh!";
let chewieRegex = /Aa*/;
let result = chewieQuote.match(chewieRegex);