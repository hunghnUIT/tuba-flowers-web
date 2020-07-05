if(isMobile()) {
    document.querySelector(".tab-mobile").style.display ="block";
    document.querySelector(".tab-desktop").style.display = "none";
} else {
    document.querySelector(".tab-mobile").style.display ="none";
    document.querySelector(".tab-desktop").style.display = "block";
}
// Get the modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
$('.thumbs-product-preview').click(function (e) { 
    e.preventDefault();
    modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
});

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}
var we = new WeNumberic('.wenumberic-product-detail', {
    stepvalue: 1,
    minvalue: 0,
    maxvalue: 100
});

var btn_description = document.querySelector("#btn-tab-description");
var btn_addinfo = document.querySelector("#btn-tab-addinfo");
var btn_review = document.querySelector("#btn-tab-review");

var tab_description = document.querySelector(".tab-description");
var tab_addinfo = document.querySelector(".tab-addinfo");
var tab_review = document.querySelector(".tab-review");

btn_description.addEventListener("click", (e) => {
    btn_description.classList.remove("active");
    btn_addinfo.classList.remove("active");
    btn_review.classList.remove("active");

    btn_description.classList.add("active");
    tab_description.style.display = "block";
    tab_addinfo.style.display = "none";
    tab_review.style.display = "none";
});

btn_addinfo.addEventListener("click", (e) => {
    btn_description.classList.remove("active");
    btn_addinfo.classList.remove("active");
    btn_review.classList.remove("active");

    btn_addinfo.classList.add("active");
    tab_description.style.display = "none";
    tab_addinfo.style.display = "block";
    tab_review.style.display = "none";
});

btn_review.addEventListener("click", (e) => {
    btn_description.classList.remove("active");
    btn_addinfo.classList.remove("active");
    btn_review.classList.remove("active");

    btn_review.classList.add("active");
    tab_description.style.display = "none";
    tab_addinfo.style.display = "none";
    tab_review.style.display = "block";
});

var RelatedProductsSwiper = new Swiper ('.related-products-container', {
    loop: true,
    slidesPerView: 4,
    breakpoints: {
        // when window width is >= 320px
        320: {
            slidesPerView: 2,
            spaceBetween: 20
        },
        // when window width is >= 480px
        480: {
            slidesPerView: 3,
            spaceBetween: 30
        },
        768: {
            slidesPerView: 4,
            spaceBetween: 30
        }
    }
});

/*TABS MOBILE SCRIPT*/
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.maxHeight){
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }
    });
}
$(document).ready(function () {
    $(".btn-add-to-cart").click(function (e) {
        var id_item = $('#id-item').text();
        var quantity = $('#quantity').val();
        if($(document).find('#user').length){
            $.ajax({
                type: "GET",
                url: "/add-to-cart/"+id_item+"-quantity="+quantity,
                cache: false,
                async: false,
                dataType: "html",
                csrfmiddlewaretoken: '{{ csrf_token }}',
                success:function(response){
                    var old_number_item_in_cart = $(document).find(".cart-number");
                    var number_item_in_cart = $(response).find(".cart-number");
                    $('.cart-number').replaceWith(number_item_in_cart)
                    if(parseInt(old_number_item_in_cart.text())===parseInt(number_item_in_cart.text())){
                        alert("Add to cart failed! This item only have "+ $(document).find("#number-item-left").text() +" items left.")
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
            window.location.replace("/login/?next=/add-to-cart/"+ id_item +"-quantity="+quantity);
        }
    });
});

$('#myModal').click(function (e) { 
    if ($(e.target).is('#img01'))
    {
        return;
    }
    else
    {
        modal.style.display = "none";
    }
});
var number_image=parseInt($('#num-image').text()) ;
var swiper = new Swiper('.preview-products-container', {
    speed:300,
    calculationHeight:true,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    slidesPerView: 3,
  });