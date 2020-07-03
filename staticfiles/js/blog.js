/**
 * Created by DELL on 4/21/2020.
 */
var blogSwiper = new Swiper ('.blog-container', {
    loop: true,
    //effect: "cube",
    // If we need pagination
    pagination: {
        el: '.blog-pagination'
    },

    // Navigation arrows
    navigation: {
        nextEl: '.blog-button-next',
        prevEl: '.blog-button-prev',
    }
});