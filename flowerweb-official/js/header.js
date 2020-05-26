
/* Search setting*/
$(document).ready(function () {
    
});
$(window).on('scroll', function () {
    $('nav').toggleClass('black', window.scrollY >250);
});
$('.modal-body').click(function (e) { 
    if ($(e.target).is('#input-group *'))
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

//var mobileHeader = document.querySelector("#mobile-header");
//var desktopHeader = document.querySelector("#desktop-header");

/*
window.addEventListener("load", (e) => {
    if(isMobile()) {
        mobileHeader.style.display = "block";
        desktopHeader.style.display = "none";

    } else {
        desktopHeader.style.display = "block";
        mobileHeader.style.display = "none";
        //document.querySelector("#mobile-header").classList.add("d-none");
        //console.log(document.querySelector("#mobile-header"));
    }
});
*/
