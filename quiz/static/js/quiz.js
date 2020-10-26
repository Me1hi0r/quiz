
btn = document.querySelector('#check_ans')
document.addEventListener('change', function() {
    let checked = document.querySelectorAll('input:checked');
    if (checked.length === 0) {
        btn.disabled = true
    } else {
        btn.disabled = false
    }
})