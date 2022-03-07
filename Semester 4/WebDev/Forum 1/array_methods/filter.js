const demo_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const another_demo_arr = [
    { name: 'karel', domicile: 'tangerang', age: 20 },
    { name: 'xiez', domicile: 'jakarta', age: 20 },
    { name: 'boris', domicile: 'semarang', age: 18 }
];

// as its name states, filter is used to filter values that is stored inside
// an array. same as the map method, this method has to be assigned into a new 
// variable to store the returned processed array. 
const res = demo_array.filter(result => result % 2 === 0);
console.log(res);

const res_2 = another_demo_arr.filter(ages => ages.age < 20);
console.log(res_2);

// additionally, map and filter can be used together 
const res_3 = another_demo_arr.filter(ages => ages.age > 18).map(domiciles => domiciles.domicile);
console.log(res_3);

const res_4 = another_demo_arr.map(ages_new => ages_new.age * 2).filter(result => result < 100);
console.log(res_4);

// modified from https://www.youtube.com/watch?v=8MoElay6dWU
