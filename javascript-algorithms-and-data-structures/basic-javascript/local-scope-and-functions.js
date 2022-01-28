function myLocalScope() {
    let myVar = 'teste';
  
    console.log('inside myLocalScope', myVar);
  }
  myLocalScope();
  
  console.log('outside myLocalScope', myVar);