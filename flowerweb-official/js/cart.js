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
    
    // add to cart ajax
    $('.btn-outline-dark').click(function (e) { 
        var idItem= $(this).find('#id-item').text();
        console.log(idItem+" added to your cart")
        $.ajax({
            type: "GET",
            url: "/add-to-cart/"+idItem+"-quantity="+1,
            cache: false,
            async: false,
            dataType: "html",
            csrfmiddlewaretoken: '{{ csrf_token }}',
            success:function(response){
                var stringQuantity =$('.cart-number').text();
                var incr_quantity=parseInt(stringQuantity)+1;
                $('.cart-number').text(incr_quantity)
                alert("Success, your cart is "+incr_quantity +" items");
            },
            error: function (xhr, textStatus, errorThrown) {
                alert(textStatus);
            },
        });
    });

    
    $('.btn-update-cart').click(function (e) { 
        e.preventDefault();
        $(".item-cart").each(function() {
            var id = $(this).find('.id-item').text();
            var quantity =$(this).find('.item-quantity').val();
            console.log(quantity);
            // compare id to what you want
            $.ajax({
                type: "GET",
                url: "/adjust-quantity/"+id+"-quantity="+quantity,
                cache: false,
                async: false,
                dataType: "html",
                csrfmiddlewaretoken: '{{ csrf_token }}',
                success:function(response){
                    alert("Success");
                },
                error: function (xhr, textStatus, errorThrown) {
                    alert(textStatus);
                },
            });
        });
        
    });
});