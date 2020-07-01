$(document).ready(function () {
    $('.shipping-cost-tr').hide();
    $('#order-btn').hide();   
    
        var isChecked = $('#customRadio').prop('checked');
        if(isChecked)
        {
            $('.shipping-cost-tr').show(1000)
            console.log("clicked")
            $('#order-btn').show(500);
        }
    $('#change-address-form').hide();
    $('#change-address-btn').click(function (e) { 
        e.preventDefault();
        $('#change-address-form').show(500);
        $('#profile-display').hide();
    });
    $('#close-form').click(function (e) { 
        e.preventDefault();
        $('#change-address-form').hide(500);
    });
});