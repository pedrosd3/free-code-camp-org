// Use as antecipações no pwRegexpara corresponder a senhas com mais de 5 caracteres e com dois dígitos consecutivos.

let sampleWord = "astronaut";
let pwRegex = /(?=\w{6,})(?=\D*\d{2,})/;
let result = pwRegex.test(sampleWord);