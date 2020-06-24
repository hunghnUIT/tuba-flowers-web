$('.icon-bar  ul  li  a').hover(function () {
        $(this).find(".cart-number").addClass("change-color-span");
        
    }, function () {
        $(this).find(".cart-number").removeClass("change-color-span");
    }
);
$(document).ready(function () {
    if ($('.box div div h2').text().length> 6 & $('.box div div h2').text().length< 12)
    {
        $('.box div div h2').css('font-size', '30px');
        console.log("title's more than 6 letters");
    }
    else if ($('.box div div h2').text().length>= 12 & $('.box div div h2').text().length<= 16)
    {
        $('.box div div h2').css('font-size', '25px');
        console.log("title's more than 12 letters");
    }
    else if ($('.box div div h2').text().length>16)
    {
        $('.box div div h2').css('font-size', '20px');
        console.log("title's more than 16 letters");
    }
    var x = 10000;
    x = x.toLocaleString('it-IT', {style : 'currency', currency : 'VND'});
    $('.price').each(function(i, obj) {
        var price= parseInt($(this).text());
        $(this).text(price.toLocaleString('it-IT', {style : 'currency', currency : 'VND'}));
    });
});