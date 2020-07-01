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

