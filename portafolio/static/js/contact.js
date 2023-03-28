function validateForm(){
    let name = document.forms['contactForm']['name'].value;
    let email = document.forms['contactForm']['email'].value;
    let subject = document.forms['contactForm']['subject'].value;
    let message = document.forms['contactForm']['message'].value;

    if (name == '' || hasNumber(name)){
        alert('El campo de nombre debe completarse y solo debe contener letras.');
        return false;
    } else if (email == '' && subject == ''){
        alert('Se debe completar el campo de correo electrónico o el campo del asunto.');
        return false;
    } else if (!(email.includes('@'))){
        alert('El correo electrónico no es válido.');
        return false;
    } else if (message == ''){
        alert('El campo de mensaje debe ser llenado.');
        return false;
    } else {
        // confirm or cancel
        return confirm('¿Quiere confirmar el envío del mensaje?')
    }
}

function hasNumber(myString) {
    return /\d/.test(myString);
}