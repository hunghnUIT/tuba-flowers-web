
/* Search setting*/
$(window).on('scroll', function () {
    $('nav').toggleClass('black', window.scrollY >250);
});
$('.modal-body').click(function (e) { 
    if ($(e.target).is('#input-group *') || $(e.target).is('.modal-change-address *'))
    {
        return;
    }
    else
    {
        $('.modal').modal('hide');
    }
});
/**
 * Created by DELL on 5/2/2020.
 */
var isMobile = function() {
    if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
        return true;
    }

    return false;
};

