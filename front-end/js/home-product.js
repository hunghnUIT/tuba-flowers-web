/**
 * Created by DELL on 5/2/2020.
 */
var new_arrival = document.querySelector("#new-arrival-tab");
var on_sale = document.querySelector("#on-sale-tab");

var new_arrival_wrapper = document.querySelector(".new-arrival-wrapper");
var on_sale_wrapper = document.querySelector(".on-sale-wrapper");
new_arrival.addEventListener("click", (e) => {
    new_arrival.classList.add("active");
    on_sale.classList.remove("active");

    new_arrival_wrapper.style.display = "block";
    on_sale_wrapper.style.display = "none";
});

on_sale.addEventListener("click", (e) => {
    new_arrival.classList.remove("active");
    on_sale.classList.add("active");

    new_arrival_wrapper.style.display = "none";
    on_sale_wrapper.style.display = "block";
});