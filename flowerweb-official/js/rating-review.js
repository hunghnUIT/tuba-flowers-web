$(document).ready(function () {
    var options = {
        max_value: 5,
        step_size: 1,
        url: 'http://localhost/test.php',
        initial_value: 5,
        update_input_field_name: $("#input2"),
    }
    $(".rate2").rate(options);

            $(".rate2").on("change", function(ev, data){
                console.log(data.from, data.to);
            });

            $(".rate2").on("updateError", function(ev, jxhr, msg, err){
                console.log("This is a custom error event");
            });

            $(".rate2").rate("setAdditionalData", {id: 42});
            $(".rate2").on("updateSuccess", function(ev, data){
                console.log(data);
            });
    var options2 = {
        max_value: 5,
        initial_value: 0,
        selected_symbol_type: 'utf8_star', // Must be a key from symbols
        cursor: 'default',
        readonly: true,
        // change_once: false, // Determines if the rating can only be set once
        ajax_method: 'POST',
        url: 'http://localhost/test.php'
        // additional_data: {} // Additional data to send to the server
    }

    $(".rating").rate(options2);
    $('.thank-content').hide();
    $(".rate2").one("click", function(ev, data){
        $('.thank-content').fadeIn(700);
    });
    
    $(".submit-comment").on("click", function(){
        var id = $(document).find("#id-item").text();
        var rate = $('.rate2').attr('data-rate-value');
        var comment = $(document).find("#comment").val();

        var csrftoken = $('meta[name="csrf-token"]').attr('content');
        $.ajax({
            type: "POST",
            url: "/add-review/",
            headers:{
                "X-CSRFToken": csrftoken
            },
            data: { 
                'id': id,
                'rate': rate, 
                'comment': comment
            },
            cache: false,
            async: false,
            dataType: "html",
            success:function(response){
                // var review_tab = $(response).find(".tab-review");
                // $('.tab-review').replaceWith(review_tab)
                window.location.reload();
                // $('html').replaceWith(response); 
            },
            error: function (xhr, textStatus, errorThrown) {
                alert(textStatus);
            },
        });
    });
});