document.getElementById("checkBtn").addEventListener("click", function () {
    let password = document.getElementById("password").value;
    let result = document.getElementById("result");

    let hasLength = password.length >= 8;
    let hasNumber = /\d/.test(password);
    let hasUppercase = /[A-Z]/.test(password);
    let hasSpecial = /[!@#$%^&*]/.test(password);

    if (hasLength && hasNumber && hasUppercase && hasSpecial) {
        result.innerHTML = "✅ Strong Password";
    } else {
        result.innerHTML = "❌ Weak Password";
    }
});