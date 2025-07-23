document.getElementById('myForm').addEventListener('submit', function(event) {
    let isValid = true;

    // Username validation
    let usernameInput = document.getElementById('editCustomername');
    let usernameError = document.getElementById('usernameError');
    if (!usernameInput.checkValidity()) {
        usernameError.textContent = "Username must be between 5 and 50 characters.";
        isValid = false;
    } else {
        usernameError.textContent = "";
    }     
    

    if (!isValid) {
        event.preventDefault(); // Prevent form submission if validation fails
    }
});