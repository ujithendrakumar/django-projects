$('document').ready(function(){
  function form_validation(){
            // alert('test');
            var username = $('#username').val();
             var fullname = $('#fullname').val();
             var email = $('#email').val();
             var phone = $('#phone').val();
             var city = $('#locality').val();
             var password = $('#password').val();
             var conform_password = $('#conform_password').val();
             var fullname = $('#fullname').val();
             var user_address = $('#user_address').val();
              only_aplhabets_pattern=/^[a-zA-Z ]*$/;
              email_pattern = /^[a-zA-Z0-9][a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
              passwordpattern=/^[A-Za-z0-9!@#$%^&*()_]{6,20}$/;
              mobile_pattern = /^[6-9]+[0-9]{9}$/;
             var str=true;
             $('#username_error,#email_error,#password_error,#phone_error,#conform_password,#city_error,#user_address_error,#fullname_error').html('');
              $('#username,#email,#password,#phone,#fullname,#conform_password,#city,#user_address').css('border','');
             if(username ==''|| username==' '){
                 str=false;
                 $('#username').css('border','1px solid red');
                 $('#username_error').css('color','red');
                 $('#username_error').html(' Please enter  name');
             } else if(!only_aplhabets_pattern.test(name)){
                 str=false;
                  $('#names').css('border','1px solid red');
                 $('#name_error').css('color','red');
                 $('#name_error').html(' Please enter valid name');
             }

             if(fullname==''|| fullname==' '){
                 str=false;
                 $('#fullname').css('border','1px solid red');
                 $('#fullname_error').css('color','red');
                 $('#fullname_error').html(' Please enter  address');
             }
             // if(phone==''|| phone==' '){
             //     str=false;
             //     $('#phone').css('border','1px solid red');
             //     $('#phone_error').css('color','red');
             //     $('#phone_error').html(' Please enter  mobile');
             // }
             // else if(!mobile_pattern.test(phone)){
             //     str=false;
             //     $('#phone').css('border','1px solid red');
             //     $('#phone_error').css('color','red');
             //     $('#phone_error').html(' Please enter valid mobile');
             // }
            // if(email==''|| email==' '){
            //      str=false;
            //      $('#email').css('border','1px solid red');
            //      $('#email_error').css('color','red');
            //      $('#email_error').html(' Please enter  email');
            //  }
            //  else if(!email_pattern.test(email)){
            //      str=false;
            //      $('#email').css('border','1px solid red');
            //      $('#email_error').css('color','red');
            //      $('#email_error').html(' Please enter valid email');
            //  }
            // alert(str);
              return str;
         }

});
