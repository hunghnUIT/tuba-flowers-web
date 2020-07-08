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

$('.detail-request').click(function (e) { 
    $('#modal-be-sure').on('show.bs.modal', function (e) {
        var detail = $('.detail-hide').text();
        $('.modal-body-sure').text(detail);
        $('.modal-title-sure').text("Detail order");
      })
    $('#request-cancel').hide();
    $('#modal-be-sure').on('hidden.bs.modal', function (e) {
        $('#request-cancel').show();
      })
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
