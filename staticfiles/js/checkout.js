$(document).ready(function () {
    $('.shipping-cost-tr').hide();
    $('#order-btn').hide();
    $('.pay-cod').click(function (e) { 
        // $('.shipping-cost-tr').css('display', 'table-row');
        var isChecked = $('#customRadio').prop('checked');
        if(isChecked)
        {
            $('.shipping-cost-tr').show(1000)
            console.log("clicked")
            $('#order-btn').show(500);
        }
    });
});