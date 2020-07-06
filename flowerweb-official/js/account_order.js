$(document).ready(function () {
    $('.my-profile-wrapper').hide();
    $('.my-order-link').click(function (e) { 
        e.preventDefault();
        $(this).addClass('active');
        $('.my-account-link').removeClass('active');
        $('.my-profile-wrapper').slideUp();
        $('.my-order-wrapper').slideDown();
        console.log("clicked-order");
    });
    $('.my-account-link').click(function (e) { 
        e.preventDefault();
        $(this).addClass('active');
        $('.my-order-link').removeClass('active');
        console.log("clicked-account");
        $('.my-profile-wrapper').slideDown();
        $('.my-order-wrapper').slideUp();
    });
});
