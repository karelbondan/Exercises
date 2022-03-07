// the reduce method is used to reduce an array into a single 
// value. for example, if we want to find the total sales of 
// a specific item. 

const sales = [
    { userID: 1, item: 'pensil', qty: 1, price: 2.5 },
    { userID: 5, item: 'baju', qty: 1, price: 200 },
    { userID: 2, item: 'pensil', qty: 3, price: 2.5 },
    { userID: 3, item: 'penghapus', qty: 1, price: 2 }
];

const total_sales_pensil =
    sales.filter(pencil => pencil.item === 'pensil')
        .map(price_fixed => price_fixed.qty * price_fixed.price)
        .reduce((total, penjualan) => total + penjualan);

console.log("the total sales for pensil is Rp " + total_sales_pensil + " ribu");

// referenced from https://www.youtube.com/watch?v=8MoElay6dWU