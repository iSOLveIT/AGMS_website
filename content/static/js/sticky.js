//Navbar shrink and navbar brand shrink
$(window).scroll(function () {
	if ($(document).scrollTop() > 50) {
		$('nav.navbar').addClass('shrink');
	}
	else {
		$('nav.navbar').removeClass('shrink');
	}
});

/* One Time Password Alert*/
$(document).ready(function(){
    // Set div display to block
    $(".init").click(function(){
        $(".OTP-main").css("display", "block");
        $("body").css("overflow-y", "hidden");
    });

    //Set div display to none
    $(".card > .card-header > button").click(function(){
        $(".OTP-main").css("display", "none");
        $("body").css("overflow-y", "scroll");
    });
});

<!-- The jquery ajax code: -->
$(function() {
    $('button#OTP_send').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + '/elearning/forms', {
        OTP_input: $('input[name="inputOTP"]').val()
      }, function(data) {
        if (data.status === 404) {
		    $("#OTP_msg").text(data.result);
            $("#OTP_alert").css("display", "block");
            $("#OTP_alert").fadeOut( 3000, "linear");
	    } else {
            $("#OTP_msg").text('Successful');
            $("#OTP_alert").css("display", "block");
            $("#OTP_alert").fadeOut( 3000, "linear", function() {
                // Animation complete.
                // similar behavior as an HTTP redirect
                window.location.replace(data.result);
            });
	    }
      });
      return false;
    });
  });

