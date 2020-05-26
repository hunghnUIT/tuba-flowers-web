$(document).ready(function () {
    $('.error-form').hide();

    var isValid_username=false;
    var isValid_phone=false;
    var isValid_email=false;
    var isValid_password=false;
    var isValid_retype=false;
    var isValid_checkbox=false;

    $('#txt-username').on('input', function () {
        checkUsername();
    });
    $('#txt-phone').on('input',function (e) { 
        checkPhone();
    });
    $('#txt-email').on('input',function (e) { 
        checkEmail();
    });
    $('#txt-password').on('input',function (e) { 
        checkPassword();
    });
    $('#txt-retype').on('input',function (e) { 
        checkRetype();
    });

    function checkUsername() {
        var pattern =/^[a-zA-Z]*$/;
        var nameInput =$('#txt-username').val();
        if(pattern.test(nameInput)&& nameInput!=""&&nameInput.length>4)
        {
            $("#name-error").hide();
            $('#txt-username').css("border-bottom","1px solid #34F458");
            isValid_username=true;
        }
        else
        {
            if (!pattern.test(nameInput))
            {
                $("#name-error").html("Should contain only characters");
                $("#name-error").show();
            }
            if (!nameInput!=""||nameInput.length<=4)
            {
                $("#name-error").html("This field must not be empty and more than 4 characters");
                $("#name-error").show();
            }
            $('#txt-username').css("border-bottom","1px solid #f90a0a");
            isValid_username=false;
        }
    }

    function checkPhone() {
        var pattern =/^[0-9]*$/;
        var phoneInput =$('#txt-phone').val();
        if(pattern.test(phoneInput)&& phoneInput!=""&& phoneInput.length ==10 )
        {
            $("#phone-error").hide();
            $('#txt-phone').css("border-bottom","1px solid #34F458");
            isValid_phone=true;
        }
        else
        {
            if (!pattern.test(phoneInput)|| phoneInput!=10)
            {
                $("#phone-error").html("Invalid phone number");
                $("#phone-error").show();
            }
            if (!phoneInput!="")
            {
                $("#phone-error").html("This field must not be empty");
                $("#phone-error").show();
            }
            $('#txt-phone').css("border-bottom","1px solid #f90a0a");
            isValid_phone=false;
        }
    }
    
    function checkEmail() {
        var pattern =/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
        var email =$('#txt-email').val();
        if(pattern.test(email)&& email!="")
        {
            $("#email-error").hide();
            $('#txt-email').css("border-bottom","1px solid #34F458");
            isValid_email=true;
        }
        else
        {
            if (!pattern.test(email))
            {
                $("#email-error").html("Invalid email");
                $("#email-error").show();
            }
            if (!email!="")
            {
                $("#email-error").html("This field must not be empty");
                $("#email-error").show();
            }
            $('#txt-email').css("border-bottom","1px solid #f90a0a");
            isValid_email=false;
        }
    }

    function checkPassword() {
        var pattern =/^[a-zA-Z0-9]*$/;
        var password =$('#txt-password').val();
        if(pattern.test(password)&& password!=""&&password.length>=5)
        {
            $("#password-error").hide();
            $('#txt-password').css("border-bottom","1px solid #34F458");
            isValid_password=true;
        }
        else
        {
            if (!pattern.test(password))
            {
                $("#password-error").html("Should contain only characters");
                $("#password-error").show();
            }
            if (!password!=""||password.length<5)
            {
                $("#password-error").html("This field must not be empty and more than 5 characters");
                $("#password-error").show();
            }
            $('#txt-password').css("border-bottom","1px solid #f90a0a");
            isValid_password=false;
        }
    }
    function checkRetype() {
        var retype =$('#txt-retype').val();
        var password=$('#txt-password').val();
        if(retype == password && retype!="")
        {
            $("#retype-error").hide();
            $('#txt-retype').css("border-bottom","1px solid #34F458");
            isValid_retype=true;
        }
        else
        {
            $("#retype-error").html("Invalid password confirm");
            $("#retype-error").show();
            $('#txt-retype').css("border-bottom","1px solid #f90a0a");
            isValid_retype=false;
        }
    }
    function checkCheckbox() {
        var checkbox =document.getElementById('vehicle2');
        if(!checkbox.checked){
            $("#checkbox-error").html("You have to agree with our terms");
            $("#checkbox-error").show();
            isValid_checkbox=false;
            console.log(isValid_checkbox);
        }else{
            $("#checkbox-error").hide();
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
    $('.submit').click(function (e) { 
        checkEmail();
        checkPassword();
        checkPhone();
        checkRetype();
        checkUsername();
        checkCheckbox();
        console.log(isValid_checkbox);
        if (!isValid_email|!isValid_password|!isValid_retype|!isValid_username|!isValid_checkbox)
        {
            alert("Please fill the form correctly");
            return false;
        }
        else
        {
            alert("Submit successfully");
            return true;
        }
    });
    $('#vehicle2').change(function(){
        if(this.checked){
            $("#checkbox-error").hide();
            isValid_checkbox=true;
            console.log(isValid_checkbox);
        }
    });

    myBlurFunction = function(state) {
    /* state can be 1 or 0 */
    var containerElement = document.getElementById('main_container');
    var overlayEle = document.getElementById('overlay');

    if (state) {
        overlayEle.style.display = 'block';
        containerElement.setAttribute('class', 'blur');
    } else {
        overlayEle.style.display = 'none';
        containerElement.setAttribute('class', null);
    }
};
});