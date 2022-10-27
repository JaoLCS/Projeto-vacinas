function form_edit(){
    var inputs = document.getElementById('create_form')
    for(var input = 0; input< inputs.length;input++){
        if(inputs[input].tagName == 'INPUT'){
            inputs[input].classList.add("form-control")
        }
    }
}

document.onload = form_edit()