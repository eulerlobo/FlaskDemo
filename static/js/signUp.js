$(function() {
    $('#btnSignUp').click(function() {
 
        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                response = JSON.parse(response);

                console.log(response);
            },
            error: function(error) {
                response = JSON.parse(response);

                console.log(error);
            }
        });
    });
});