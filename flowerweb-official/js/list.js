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

        $.ajax({
            type: "GET",
            url: "/products/?order_by="+ item,
            cache: false,
            async: false,
            dataType: "html",
            csrfmiddlewaretoken: '{{ csrf_token }}',
            success:function(response){
                 html = response;
                var htmlFiltered = $(response).find(".result");    
                //console.log(htmlFiltered); 
                $('.append-result').html(htmlFiltered);
            },
            error: function (xhr, textStatus, errorThrown) {
                alert(textStatus);
            },
        });
    });
});