$('.icon-bar > a').hover(function () {
        $(this).find("span").addClass("change-color-span");
        
    }, function () {
        $(this).find("span").removeClass("change-color-span");
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
    if ($('#cart').length > 0) {
        $('.title >div').css('background-image', "url('../flowerweb-official/images/cart/cart-landscape.png')");
    }
    else if ($('#detail').length > 0)
    {
        $('.title >div').css('background-image', "url('../flowerweb-official/images/product-detail/product-landscape.png')");
    }
    else if ($('#list').length > 0)
    {
        $('.title >div').css('background-image', "url('../flowerweb-official/images/product-list/list-landscape.png')");
    }
});