
const showPasswordToggle = document.querySelector(".showPasswordToggle");
const handleToggleInput = (e) => {
  if (showPasswordToggle.textContent === "SHOW") {
    showPasswordToggle.textContent = "HIDE";
    passwordField.setAttribute("type", "text");
  } else {
    showPasswordToggle.textContent = "SHOW";
    passwordField.setAttribute("type", "password");
  }
};

showPasswordToggle.addEventListener("click", handleToggleInput);



let btn = document.querySelector('#reg_btn');

document.addEventListener('change', function() {
    let user_name = document.querySelector('#usernameField');
    let password = document.querySelector('#passwordField');
    if(user_name.value !== '' && password.value !== ''){
        btn.disabled = false;
    } else {
        btn.disabled = true;
    }
});