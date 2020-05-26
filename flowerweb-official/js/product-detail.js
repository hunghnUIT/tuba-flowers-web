if(isMobile()) {
    document.querySelector(".tab-mobile").style.display ="block";
    document.querySelector(".tab-desktop").style.display = "none";
} else {
    document.querySelector(".tab-mobile").style.display ="none";
    document.querySelector(".tab-desktop").style.display = "block";
}

var galleryThumbs = new Swiper('.gallery-thumbs', {
    direction: 'vertical',
    spaceBetween: 10,
    slidesPerView: 3,
    freeMode: true,
    watchSlidesVisibility: true,
    watchSlidesProgress: true
});

var galleryTop = new Swiper('.gallery-top', {
    spaceBetween: 10,

    thumbs: {
        swiper: galleryThumbs
    }
});

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

