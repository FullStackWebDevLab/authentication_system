const URL = "http://127.0.0.1:5000";

const showSignup = document.getElementById("showSignup");
const signupForm = document.getElementById("signupForm");
const signupButton = document.getElementById("signupButton");

const showLogin = document.getElementById("showLogin");
const loginForm = document.getElementById("loginForm");
const loginButton = document.getElementById("loginButton");

// Switch between login and signup forms.
showLogin.addEventListener("click", (event) => {
    event.preventDefault();
    loginForm.classList.remove("hidden");
    signupForm.classList.add("hidden");
});

showSignup.addEventListener("click", (event) => {
    event.preventDefault();
    signupForm.classList.remove("hidden");
    loginForm.classList.add("hidden");
});

// Signup.
signupButton.addEventListener("click", async (event) => {
    event.preventDefault()

    const username = document.getElementById("signupUsername").value;
    const email = document.getElementById("signupEmail").value;
    const password = document.getElementById("signupPassword").value;

    const response = await fetch(`${URL}/signup`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "username": username,
            "email": email,
            "password": password
        })
    });
    
    text = await response.text();
    console.log(text);
});

// Login
loginButton.addEventListener("click", async (event) => {
    event.preventDefault()

    const username = document.getElementById("loginUsername").value;
    const password = document.getElementById("loginPassword").value;

    const response = await fetch(`${URL}/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "username": username,
            "password": password
        })
    });
    
    const text = await response.text();
    console.log(text);
});
