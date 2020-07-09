var btnViewDetails = document.querySelectorAll(".btn-view-detail");

btnViewDetails.forEach((item) => {
   item.addEventListener("click", (e) => {
       document.querySelector(".popup-detail-order").classList.remove("d-none");
   });
});

document.querySelector(".btn-discard-close").addEventListener("click", (e) => {
    document.querySelector(".popup-detail-order").classList.add("d-none");
 });
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

    $('#modal-be-sure').on('show.bs.modal', function (e) {
		var url_request = $(e.relatedTarget).data('id');
       // Do Whatever you like to do,
       $('.modal-body-sure').text("Wanna request cancel?");
        $('.modal-title-sure').text("Confirmation");
       $('#request-cancel').click(function (e) { 
           e.preventDefault();
           $.ajax({
            type: "GET",
            url: url_request,
            cache: false,
            async: false,
            dataType: "html",
            csrfmiddlewaretoken: '{{ csrf_token }}',
            success:function(response){
                window.location.replace("/user/profile")
            },
            error: function (xhr, textStatus, errorThrown) {
                // alert(textStatus);
            },
        });
       });
	 });
});
