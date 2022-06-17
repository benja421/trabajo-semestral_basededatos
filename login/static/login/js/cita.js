var expr = /^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$/;
$(document).ready(function(){
$("#mensajecita").submit(function(e){
    e.preventDefault();
    
    var dueno = $("#nombredueno").val();
    var mascota= $("#nombremas").val();
    var correo = $("#correo").val();
    
    let mensajemostrar = "";
    let entrar = false;

    if(dueno.trim().length < 4 ){
        mensajemostrar += "La longitud no es correcta<br>";
        entrar = true;
    }

    

    if(entrar){
        $("#mensajecita").html(mensajemostrar);
    }
    else{
        $("#mensajecita").html("formulario enviado")
    }

})


})