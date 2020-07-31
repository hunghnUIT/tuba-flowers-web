$(document).ready(function () {
    var options = {
        max_value: 5,
        step_size: 1,
        url: 'http://localhost/test.php',
        initial_value: 1,
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
        step_size: 0.5,
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
    console.log($(".rate2").rate("getValue"));
});