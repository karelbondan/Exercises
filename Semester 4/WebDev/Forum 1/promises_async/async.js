// some basic functions to log in a user and displays 
// their name afterwards.
function login(email, password) {
    return new Promise((resolve, reject) => {
        // simulating loading time on server, in this case
        // 2 secs.
        setTimeout(() => {
            const success = true;

            if (success) {
                resolve({ userEmail: email });
            }
            else {
                reject('Error: Something unexpected happened');
            }
        }, 2000);
    })
}

function getProfile(email) {
    return new Promise((resolve, reject) => {
        // simulating loading time on server. in this case 
        // 1,5 secs.
        setTimeout(() => {
            const success = true;

            if (success) {
                resolve({ name: 'karel', domicile: 'tangerang', birth: '301201' });
            }
            else {
                reject('Error: Something unexpected happened');
            }
        }, 1500);
    })
}

// the function below works just fine, but will result 
// in undefined because the server hasn't finished 
// doing the task but the client has already requested 
// to go on to the next statement, which is calling the 
// getProfile function, thus passing undefined.
/*
function loginDisplay() {
    const signin = login('a@a.com', 'askdjaksldj');
    const profile = getProfile(signin.userEmail);
    console.log(profile.name);
}
*/

// async await is the fix for that
async function loginDisplay() {
    const signin = await login('a@a.com', 'askdjaksldj');
    const profile = await getProfile(signin.userEmail);
    console.log(profile.name);
}

loginDisplay();

// modified from: https://www.youtube.com/watch?v=_8gHHBlbziw