function reverseString(str) {
  let stringReversa = '';

  for(let i = str.length - 1; i >= 0; i--){
    stringReversa += str[i];
  }

  return stringReversa
}

reverseString("hello");