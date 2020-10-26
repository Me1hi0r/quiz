
let btn = document.querySelector('#login_btn');

document.addEventListener('change', function() {
    let user_name = document.querySelector('#usernameField');
    let password = document.querySelector('#passwordField');
    if(user_name.value !== '' && password.value !== ''){
        btn.disabled = false;
    } else {
        btn.disabled = true;
    }
});