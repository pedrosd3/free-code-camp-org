let foods = {
    apples: 25,
    oranges: 32,
    plums: 28
};

foods.bananas = 13; // 1° way to add a new property

foods['grapes'] = 35; // 2° way to add a new property

let newFoodName = 'strawberries';
foods[newFoodName] = 27; // 3° way to add a new property

console.log(foods);