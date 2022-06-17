$(document).ready(function(){
    $("#formini").submit(function(e){
        e.preventDefault();
        
        var correose = $("#emailse").val();
        var passsec = $("#passsec").val();
        let loginmen = "";
        let login = false;

        if(correose != "test@gmail.cl"){
            loginmen +="correo o contraseña no validos";
            login =true;
        }
        if(passsec != "test"){
            loginmen +="correo o contraseña no validos";
            login =true;
        }

        if(login){
            $("#mensajesec").html(loginmen);
        }
        else{
            $("#mensajesec").html("inicio de sesion exitoso")
        }


    })
})
