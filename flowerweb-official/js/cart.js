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
    $(document).on("click",".btn-outline-dark", function(){
        var idItem= $(this).find('#id-item').text();
        // if(authenticated) -> ajax below.
        // else: window.location.replace('/login')
        if($(document).find('#user').length){
            console.log('User')
            console.log(idItem+" added to your cart");
            $.ajax({
                type: "GET",
                url: "/add-to-cart/"+idItem+"-quantity="+1,
                cache: false,
                async: false,
                dataType: "html",
                csrfmiddlewaretoken: '{{ csrf_token }}',
                success:function(response){
                    // var stringQuantity =$('.cart-number').text();
                    // var incr_quantity=parseInt(stringQuantity)+1;
                    // $('.cart-number').text(incr_quantity)
                    var old_number_item_in_cart = $(document).find(".cart-number");
                    console.log(old_number_item_in_cart.text());
                    var number_item_in_cart = $(response).find(".cart-number");
                    $('.cart-number').replaceWith(number_item_in_cart)
                    if(parseInt(old_number_item_in_cart.text())===parseInt(number_item_in_cart.text())){
                    alert("Add to cart failed! This item's number is not enough.")
                    } else{
                        alert("Success, your cart is having "+number_item_in_cart.text() +" items now.");
                    }
                },
                error: function (xhr, textStatus, errorThrown) {
                    alert(textStatus);
                },
            });
        }
        else{
            console.log('Visitor');
            window.location.replace("/login/?next=/add-to-cart/"+ idItem +"-quantity=1");
        }
    });

    
    // Remove item in cart view ajax
    $(document).on("click",".btn-remove-from-cart", function(){
        console.log(this.value);//Put link into value equal to href in <a>
        $.ajax({
            type: "GET",
            url: this.value,
            cache: false,
            async: false,
            dataType: "html",
            csrfmiddlewaretoken: '{{ csrf_token }}',
            success:function(response){
                var number_item_in_cart = $(response).find(".cart-number");
                $('.cart-number').replaceWith(number_item_in_cart) 
                var cart = $(response).find("#table-cart-items");
                $('#table-cart-items').replaceWith(cart)    
                var div_cart_total = $(response).find(".cart-total");
                $('.cart-total').replaceWith(div_cart_total)
                var summary_total = $(response).find("#summary-total");
                $('#summary-total').replaceWith(summary_total)
            },
            error: function (xhr, textStatus, errorThrown) {
                alert(textStatus);
            },
        });
    });

    // Update cart Ajax
    $('#btn-update-cart').click(function (e) { 
        e.preventDefault();
        $(".item-cart").each(function() {
            var id = $(this).find('.id-item').text();
            var quantity =$(this).find('.item-quantity').val();
            var number_remain = $(this).find('.number-remain').text();
            if(parseInt(quantity)>parseInt(number_remain)){
                alert("We don't have enough item: "+ $(this).find('.item-title').text());
            }
            else{
                $.ajax({
                    type: "GET",
                    url: "/adjust-quantity/"+id+"-quantity="+quantity,
                    cache: false,
                    async: false,
                    dataType: "html",
                    csrfmiddlewaretoken: '{{ csrf_token }}',
                    success:function(response){
                        var number_item_in_cart = $(response).find(".cart-number");
                        $('.cart-number').replaceWith(number_item_in_cart)  
                        var cart = $(response).find("#table-cart-items");
                        $('#table-cart-items').replaceWith(cart)    
                        var div_cart_total = $(response).find(".cart-total");
                        $('.cart-total').replaceWith(div_cart_total)
                        var summary_total = $(response).find("#summary-total");
                        $('#summary-total').replaceWith(summary_total)
                        var div_coupon = $(response).find(".coupon");
                        $('.coupon').replaceWith(div_coupon)
                    },
                    error: function (xhr, textStatus, errorThrown) {
                        alert(textStatus);
                    },
                });
            }
        });
        
    });
});

// btn-apply-coupon
$(document).on("click","#btn-apply-coupon", function(){
    var coupon = $(this).parent().find('#coupon-input').val();
    console.log(coupon)
    if (coupon == ""){
        $( "#btn-apply-coupon" ).before( '<div class="alert alert-danger mt-3" role="alert">You have to enter the coupon first.</div>' );
        $(".alert .alert-danger").text('Test message here');
    }
    else{
        $.ajax({
            type: "GET",
            url: "/add-coupon/"+coupon,
            cache: false,
            async: false,
            dataType: "html",
            csrfmiddlewaretoken: '{{ csrf_token }}',
            success:function(response){
                var div_coupon = $(response).find(".coupon");
                $('.coupon').replaceWith(div_coupon)
                var cart = $(response).find("#table-cart-items");
                $('#table-cart-items').replaceWith(cart) 
                var div_cart_total = $(response).find(".cart-total");
                $('.cart-total').replaceWith(div_cart_total)
            },
            error: function (xhr, textStatus, errorThrown) {
                alert(textStatus);
            },
        });
    }
});

// When client focus out the quantity box.
$(".item-quantity").focusout(function(){
    var quantity = $(this).val();
    var number_remain = $(this).parent().find('.number-remain').text();
    if(parseInt(quantity)){
        if(quantity > number_remain){
            $(this).val(parseInt(number_remain)) 
        }
        else if(quantity<0){
            $(this).val(1);
        }
    }
    else{
        $(this).val(1);
    }
    
});