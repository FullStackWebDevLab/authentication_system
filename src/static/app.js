const URL = "http://127.0.0.1:5000";
const signupButton = document.getElementById("signupButton");
signupButton.addEventListener("click", signup)

async function signup(event) {
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
}
