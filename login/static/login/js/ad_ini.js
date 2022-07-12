$(document).ready(function(){
    $("#formad").submit(function(e){
        
        
        var correo = $("#emailadm").val();
        var pass = $("#passadm").val();
        let loginmen = "";
        let login = false;

        if(correo != "test@gmail.cl"){
            loginmen +="correo o contraseña no validos";
            login =true;
        }else{
            loginmen +="bienvenido";
        }

        if(pass != "test"){
            loginmen +="correo o contraseña no validos";
            login =true;
        }else{
            loginmen +="bienvenido";
        }

        if(login){
            $("#loginadm").html(loginmen);
        }
        else{
            $("#loginadm").html("inicio de sesion exitoso")
        }

    })
})