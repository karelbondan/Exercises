// this creates a const array consisting of js objects that will be later 
// published into the body of the page as lists.
const posts = [
    { title: 'Post One', body: 'This is post one' },
    { title: 'Post Two', body: 'This is post two' }
];

// creates a function that will append the objects inside the posts array into
// the body of the webpage.
function getPosts() {
    // setTimeout here is used as a demo when the page is sending request and receiving 
    // the result from the server, see it as a loading time for the page. 
    setTimeout(() => {
        // declares a new empty string variable.
        let output = '';
        // enhanced for loop for js arrays, which in this case will append the 'title'
        // inside the posts array into a list that will be displayed in the body of 
        // the webpage.
        posts.forEach((post, index) => {
            output += `<li>${post.title}</li>`
        });
        // sets the body of the page to the modified output variable.
        document.body.innerHTML = output;
        // the simulated waiting time for this to reload the page is 1 second.
    }, 1000);
}

// function to append the items inside the posts array into the body of the page.
function createPost(post) {
    // returns a new promise, which accepts resolve and reject functions. they 
    // are pretty much self explanatory.
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            // append a new js object into the posts array.
            posts.push(post);

            // error variable to simulate resolve and reject.
            const err = false;

            // if not error then end the function with resolve, else show
            // an error message with the reject function.
            if (!err) {
                resolve()
            }
            else {
                reject('Error: Something unexpected happened.')
            }
            // the simulated wait time is 3 seconds.
        }, 2000)
    })
}

// call the createPost function with a new js object as parameter to be then appended into the 
// posts array, then after it finishes calls the getPosts function to set the body of the webpage 
// to include the contents inside the posts array, afterwards if there's an error and Promise calls 
// the reject function, then catch it properly using the catch function below. In this case, it will 
// show what is the error message the Promise emitted, then displays it on the console. 
createPost({ title: 'Post Three', body: 'This is post three' })
    .then(getPosts)
    .catch(err => console.log(err));

// a bunch of resolve variables to be then showed when Promise calls the resolve function. 
const promise1 = Promise.resolve('Hello world! I have been resolved');
const promise2 = Promise.resolve('Hello universe! This is resolve two');
const promise3 = new Promise((resolve, reject) => setTimeout(resolve, 2000, 'bye'));

// sets what the resolve function going to do (in this case just stores the promise variables 
// defined earlier, it can do other stuff such as calling another function and do some other things), 
// then in this case displays the values of what the resolve function going to produce to 
// the console. 
Promise.all([promise1, promise2, promise3]).then((values) => console.log(values));

//modified from: https://www.youtube.com/watch?v=PoRJizFvM7s