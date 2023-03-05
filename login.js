
function login() {
    var username = Document.getElementById("username").value;
    var password = Document.getElementById("password").value;
    if (username === "rg" && password === "12345") {
        alert("You have successfully logged in.");
    } else {
        alert("wrong credentials");
    }
}