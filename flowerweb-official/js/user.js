$('.input').focus(function () {
    $(this).parent().parent().addClass('focus');
}).blur(function () {
    console.log();
    if($(this).val()=="")
    {
        $(this).parent().parent().removeClass('focus');
        $(this).parent().parent().children('.notice').removeClass('show');
        $(this).parent().parent().children('.notice').children('.tooltip-text').html("");
    }
});

$(document).ready(function () {
    $('#register').hide();
    $('#go-to-login').click(function (e) { 
        $('#register').hide();
        $('#login').fadeIn(1000);
       //$('#login').animate({opacity:100,marginRight:360});
    });
    $('#create-account').click(function (e) { 
        $('#login').hide();
        $('#register').fadeIn(1000);
    });
});