// getting data from an API in a form of JSON 
// then displaying it to the console
fetch('https://reqres.in/api/users')
    .then(res => res.json())
    .then(data => console.log(data));

// fetch will always be successful when getting
// data from an API, thus we catch the request 
// error inside the first then rather than manually 
// calling the catch function. the catch function can be 
// useful if we're trying to catch other things related
// to client such as network error.
fetch('https://reqres.in/api/users')
    .then(res => {
        if (res.ok) {
            console.log('acquired data succesfully');
            return res.json();
        } else {
            console.log('something unexpected happened');
        }
    })
    .then(data => console.log(data))
    .catch('Error: Please check your network connection');

// there's another additional function in fetch
// which is what we're going to do with the url we 
// passed onto it. we can do some http stuff such as get,
// post, put, delete, etc. in this case, we're doing a post
// method. additional name-value must be passed into the additional
// function (headers and JSON.stringify) to properly tell what we're
// working with, in this case a JSON object.
fetch('https://reqres.in/api/users', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        name: 'karel'
    })
}).then(res => res.json())
    .then(data => console.log(data))
    .catch('Error: Please chekc your network connection');

// modified from: https://www.youtube.com/watch?v=cuEtnrL9-H0