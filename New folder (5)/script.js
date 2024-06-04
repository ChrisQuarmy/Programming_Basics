const input= Document.querySelector(".input_field");
const inputIcon= Document.querySelector(".input_Icon");

InputIcon.addEventListener("click", e => {
    e.preventDefault();

    inputIcon.setAttribute(
        'src',
        input.getAttribute('type') === 'password' ?
        '/scr/hidden.png'
        :
        'scr/visibility.png'
    );
    input.setAttribute(
        'type',
        onput.getAttribute('type') === 'password' ?
        'type'
        :
        'Password'
    );
})