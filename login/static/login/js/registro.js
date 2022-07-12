
$(document).ready(function(){
$("#formulario").submit(function(e){
    

    const str = undefined;
    str.trim();

    var pass1 = $("#pass").val();
    var pass2 = $("#passr").val();
    var nomb = $("#nombre").val();
    var ape = $("#apellido").val();

    let mensajemostrar = "";
    let entrar = false;

    

    if(nomb.trim().length < 2){
        mensajemostrar += "* El nombre tiene un minimo de 3 caracteres";
        entrar = true;
    }
    if(nomb.trim().length > 30){
        mensajemostrar += "* El nombre exede los 30 caracteres";
        entrar = true;
    }

    if(ape.trim().length < 3){
        mensajemostrar += "* El apellido tiene un minimo de 3 caracteres";
        entrar = true;
    }

    if(ape.trim().length > 30){
        mensajemostrar += "* El apellido exede los 30 caracteres";
        entrar = true;
    }

    if( pass1 != pass2) {
        mensajemostrar += "* Las contraseñas no coinsiden";
        entrar = true;

    }
    if(pass1.trim().length < 5 ){
        mensajemostrar += "* La contraseña debe tener minimo 5 ";
        entrar = true;
    }

    if(pass1.trim().lenght > 16){
        mensajemostrar += "* La contraseña debe ser menor 16 caracteres";
        entrar = true;
    }
   
    if(entrar){
        $("#mensaje").html(mensajemostrar);
    }
    else{

    }

    
})


})