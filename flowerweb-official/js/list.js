$(document).ready(function () {
//     $.ajaxSetup({ 
//         beforeSend: function(xhr, settings) {
//             function getCookie(name) {
//                 var cookieValue = null;
//                 if (document.cookie && document.cookie != '') {
//                     var cookies = document.cookie.split(';');
//                     for (var i = 0; i < cookies.length; i++) {
//                         var cookie = jQuery.trim(cookies[i]);
//                         // Does this cookie string begin with the name we want?
//                         if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                             break;
//                         }
//                     }
//                 }
//                 return cookieValue;
//             }
//             if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
//                 // Only send the token to relative URLs i.e. locally.
//                 xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
//             }
//         } 
//    });
    $(".custom-select").change(function () {
        var item = $(this).find(":selected").val();
        var type = $(document).find("#filter-page-with").text();
        var kwarg = $(document).find("#kwarg").text();
        if(type !== "/search/"){
            type = "/products/" + type;
            kwarg = kwarg + "?";
        }
        else{
            kwarg = "?q=" + kwarg +"&"
        }
        var url = type + kwarg + "order_by="+ item;
        $.ajax({
            type: "GET",
            url: url,
            cache: false,
            async: false,
            dataType: "html",
            csrfmiddlewaretoken: '{{ csrf_token }}',
            success:function(response){
                html = response;
                var htmlFiltered = $(response).find(".result");    
                //console.log(htmlFiltered); 
                $('.append-result').html(htmlFiltered);
                var pagination = $(response).find('.pagination');
                $('.pagination').replaceWith(pagination);
            },
            error: function (xhr, textStatus, errorThrown) {
                alert(textStatus);
            },
        });
    });

    
});
var swiper = new Swiper('.topics-container', {
    speed:300,
    calculationHeight:true,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    slidesPerView: 5,
  });