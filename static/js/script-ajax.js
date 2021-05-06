
$(document).ready(function(){
    console.log("loaded");
//    $.material.init();

    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();

        var form = $('#register-form').serialize();
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response);
            }
        });
    });

    $(document).on("submit", "#login-form", function(e){
        e.preventDefault();

        var form = $('#login-form').serialize();
        $.ajax({
            url: '/checklogin',
            type: 'POST',
            data: form,
            success: function(res){
                if(res == "error"){
                    alert("Could not Log-In");
                }
                else{
                    console.log("Logged In as ", res);
                    window.location.href = "/";
                    }
            }
        });
    });
    $(document).on('click', '#logoutlink', function(e){
        e.preventDefault();
        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function(res){
                if (res == 'success'){
                    window.location.href = '/login';
                    }
                else{
                    alert("Something went wrong");
                    }
            }
        });
    });
    $(document).on("submit","#postactivity", function(e){
        e.preventDefault()
        form = $(this).serialize();

        $.ajax({
            url: '/postactivity',
            type: 'POST',
            data: form,
            success: function(res){
                console.log(res);
                }
            });
        });

    $(document).on("submit","#updateform", function(e){
        e.preventDefault();

        var form = $(this).serialize();
        $.ajax({
            url: '/updateform',
            type: 'POST',
            data: form,
            success: function(res){
                if(res == "success"){
                    window.location.href = window.location.href;
                }else{
                    alert(res);
                     }
                }
            })
        });
});


