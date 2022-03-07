const demo_array = [1, 2, 3, 4, 5, 6, 7];
const another_demo_arr = [
    { name: 'karel', domicile: 'tangerang', age: 20 },
    { name: 'xiez', domicile: 'jakarta', age: 20 },
    { name: 'boris', domicile: 'semarang', age: 18 }
];

// map is a method to return a new array based on the thing we're doing 
// to the array, so basically it is to return a new array that have been modified 
// based on what we're gonna do with it. a new variable must be assigned to store
// the returned array from the map method.
const new_array = demo_array.map(Math.sqrt);
console.log(new_array);

const new_new_array = demo_array.map(result => {
    return result * 100 / 5
});
console.log(new_new_array);

// when used in js objects, map can be used 
// to "flatten" them and store them in a new array. in this case,
// map is used to take the 'name' values from the objects inside the array.
const names = another_demo_arr.map(nama => nama.name);
console.log(names);

// modified from https://www.youtube.com/watch?v=8MoElay6dWU and https://www.youtube.com/watch?v=EzB6Pk66XW8