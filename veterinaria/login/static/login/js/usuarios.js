$(document).ready(function(){
$("#usario_datos").click(function () {

    var url = "https://randomuser.me/api/?inc=id,name,email,dob";

    informacion(url);

    function informacion(url){
        fetch(url).then((response) => (response.json())).then(function(data){

            $.each(data.results, function(i, item) {
                $("#tabla_usuarios").append("<tr><td>" + item.id.value+
                            "</td><td>" + item.name.first+ " " + item.name.last +
                            "</td><td>"+ item.email +
                            "</td><td>" + item.dob.date +
                            "</td></tr>");
            });

        })
    }
})
})

