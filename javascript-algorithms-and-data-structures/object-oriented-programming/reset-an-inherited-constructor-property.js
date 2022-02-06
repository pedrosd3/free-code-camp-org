function Animal() {}

function Bird() {}

function Dog() {}

Bird.prototype = Object.create(Animal.prototype);
Dog.prototype = Object.create(Animal.prototype);

let duck = new Bird();
let beagle = new Dog();

Bird.prototype.constructor = Bird;
duck.constructor;

Dog.prototype.constructor = Dog;
beagle.constructor;