$(document).ready(function () {
    $('#more-info-sign-in').hide();
    $('.not-empty-allow').hide();
    var isValid_username=false;
    var isValid_phone=false;
    var isValid_email=false;
    var isValid_password=false;
    var isValid_retype=false;
    var isValid_checkbox=false;
    var isValid_firstName=false;
    var isValid_lastName=false;
    var isValid_address=false;

    $('#txt-username').on('input', function (e) {
        checkUsername($(this));
    });
    $('#txt-phone').on('input',function (e) { 
        checkPhone($(this));
    });
    $('#txt-email').on('input',function (e) { 
        checkEmail($(this));
    });
    $('#txt-password').on('input',function (e) { 
        checkPassword($(this));
    });
    $('#txt-retype').on('input',function (e) { 
        checkRetype($(this));
    });
    
    $('#txt-first-name').on('input',function (e) { 
        checkFirstName($(this));
    });
    $('#txt-last-name').on('input',function (e) { 
        checkLastName($(this));
    });
    $('#txt-address').on('input',function (e) { 
        checkAddress($(this));
    });

    function checkUsername(para) {
        var pattern =/^[a-zA-Z0-9]*$/;
        var nameInput =$('#txt-username').val();
        const temp=para.parent().parent().children('.notice');
        if(pattern.test(nameInput)&& nameInput!=""&&nameInput.length>4)
        {
            temp.removeClass('show');
            isValid_username=true;
        }
        else
        {
            if (!pattern.test(nameInput))
            {
                temp.addClass('show');
                temp.children('.tooltip-text').html("Invalid name")
            }
            if (!nameInput!=""||nameInput.length<=4)
            {
                temp.addClass('show');
                temp.children('.tooltip-text').html("More than 4 characters")
            }
            isValid_username=false;
        }
    }

    function checkPhone(para) {
        var pattern =/^[0-9]*$/;
        var phoneInput =$('#txt-phone').val();
        const temp=para.parent().parent().children('.notice');
        if(pattern.test(phoneInput)&& phoneInput!=""&& phoneInput.length ==10 )
        {
            temp.removeClass('show');
            isValid_phone=true;
        }
        else
        {
            if (!pattern.test(phoneInput)|| phoneInput!=10)
            {
                temp.addClass('show');
                temp.children('.tooltip-text').html("Invalid phone number");
            }
            if (!phoneInput!="")
            {
                temp.addClass('show');
                temp.children('.tooltip-text').html("Must not be empty");
            }
            isValid_phone=false;
        }
    }
    function checkEmail(para) {
        var pattern =/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
        var email =$('#txt-email').val();
        const temp=para.parent().parent().children('.notice');
        if(pattern.test(email)&& email!="")
        {
            temp.removeClass('show');
            isValid_email=true;
        }
        else
        {
            if (!pattern.test(email))
            {
                temp.addClass('show');
                temp.children('.tooltip-text').html("Invalid e-mail");
            }
            if (!email!="")
            {
                temp.addClass('show');
                temp.children('.tooltip-text').html("Must not be empty");
            }
            isValid_email=false;
        }
    }

    function checkPassword(para) {
        var pattern =/^[a-zA-Z0-9]*$/;
        var password =$('#txt-password').val();
        const temp=para.parent().parent().children('.notice');
        if(pattern.test(password)&& password!=""&&password.length>=5)
        {
            temp.removeClass('show');
            isValid_password=true;
        }
        else
        {
            if (!pattern.test(password))
            {
                temp.addClass('show');
                temp.children('.tooltip-text').html("Include invalid character");
            }
            if (!password!=""||password.length<5)
            {
                temp.addClass('show');
                temp.children('.tooltip-text').html("More than 5 characters");
            }
            isValid_password=false;
        }
    }
    function checkRetype(para) {
        var retype =$('#txt-retype').val();
        var password=$('#txt-password').val();
        const temp=para.parent().parent().children('.notice');
        if(retype == password && retype!="")
        {
            temp.removeClass('show');
            isValid_retype=true;
        }
        else
        {
            temp.addClass('show');
            temp.children('.tooltip-text').html("Password do not match");
            isValid_retype=false;
        }
    }

    function checkFirstName(para) {
        var pattern =/^[a-zA-Z]*$/;
        var firstName =$('#txt-first-name').val();
        const temp=para.parent().parent().children('.notice');
        if(pattern.test(firstName)&& firstName!="")
        {
            temp.removeClass('show');
            isValid_firstName=true;
        }
        else
        {
            temp.addClass('show');
            temp.children('.tooltip-text').html("Invalid name");
            isValid_firstName=false;
        }
    }
    function checkLastName(para) {
        var pattern =/^[a-zA-Z]*$/;
        var lastName =$('#txt-last-name').val();
        const temp=para.parent().parent().children('.notice');
        if(pattern.test(lastName)&& lastName!="")
        {
            temp.removeClass('show');
            isValid_lastName=true;
        }
        else
        {
            temp.addClass('show');
            temp.children('.tooltip-text').html("Invalid name");
            isValid_lastName=false;
        }
    }
    function checkAddress(para) {
        var address =$('#txt-address').val();
        const temp=para.parent().parent().children('.notice');
        if(address!="")
        {
            temp.removeClass('show');
            isValid_address=true;
        }
        else
        {
            temp.addClass('show');
            temp.children('.tooltip-text').html("Not be empty");
            isValid_address=false;
        }
    }

    function checkCheckbox() {
        var checkbox =document.getElementById('vehicle2');
        if(!checkbox.checked){
            $('.submit').prop('disable',true)
            isValid_checkbox=false;
            console.log(isValid_checkbox);
        }else{
            $('.submit').prop('disable',false)
            isValid_checkbox=true;
            console.log(isValid_checkbox);

        }
    }
    $('#txt-moreinfo').click(function (e) {
        if($('#txt-moreinfo').val()=="Optional...")
        {$('#txt-moreinfo').val("");}
    });
    $('#txt-moreinfo').focusout(function (e) { 
        if( $('#txt-moreinfo').val()=="")
        {$('#txt-moreinfo').val("Optional...");}
    });
    $('.register-btn').click(function (e) { 
        console.log(isValid_checkbox);
        if (!isValid_email|
            !isValid_password|
            !isValid_retype|!isValid_username|
            !isValid_checkbox|
            !isValid_firstName|
            !isValid_lastName|
            !isValid_address)
        {
            if (!isValid_checkbox)
            {
                alert("Please agree to our terms and conditions");
            }
            
        }
        else
        {
            
            return true;
        }
    });
    $('#vehicle2').change(function(){
        if(this.checked){
            $("#checkbox-error").hide();
            isValid_checkbox=true;
            console.log(isValid_checkbox);
            $('.register-btn').prop('disabled', false);
        }
        else
        {
            isValid_checkbox=false;
            $('.register-btn').prop('disabled', true);
        }
    });
    $('.login-btn').click(function (e) { 
        e.preventDefault();
    });
    
    var isChecked = $('#vehicle2').prop('checked');
    if (!isChecked){
        $('.register-btn').prop('disabled', true);
    }
    else{
        $('.register-btn').prop('disabled', false);
    }
    $(".next-btn").click(function (e) { 
        e.preventDefault();
        if (!isValid_email|!isValid_password|!isValid_retype|!isValid_username)
        {
            $('.not-empty-allow').show();
           return false;
        }
        else
        {
            $('.not-empty-allow').hide();
            $('#sign-in-info').fadeOut(500);
            $('#more-info-sign-in').fadeIn(500);
            return true;
        }
    });
    $('.previous-step').click(function (e) { 
        e.preventDefault();
        $('#sign-in-info').slideDown(500);
        $('#more-info-sign-in').slideUp(500);
    });
});