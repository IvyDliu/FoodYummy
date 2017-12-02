$(document).ready(function(){

	$("#navigation").sticky({
		topSpacing : 75,
	});

	// $('#nav').onePageNav({
    // 	currentClass: 'current',
    // 	changeHash: false,
    // 	scrollSpeed: 15000,
    // 	scrollThreshold: 0.5,
    // 	filter: '',
    // 	easing: 'easeInOutExpo'
    // });

    //  $('#top-nav').onePageNav({
    //      currentClass: 'active',
    //      changeHash: true,
    //      scrollSpeed: 1200
    // });
//Initiat WOW JS
    new WOW().init();

    $('.slick-slider').slick({
        dots: true,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        centerMode: true,
        variableWidth: true,
        autoplay: true
    });

        // Add smooth scrolling to all links
        $("a").on('click', function(event) {

            // Make sure this.hash has a value before overriding default behavior
            if (this.hash !== "") {
                // Prevent default anchor click behavior
                event.preventDefault();

                // Store hash
                var hash = this.hash;

                // Using jQuery's animate() method to add smooth page scroll
                // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
                $('html, body').animate({
                    scrollTop: $(hash).offset().top
                }, 800, function(){

                    // Add hash (#) to URL when done scrolling (default click behavior)
                    window.location.hash = hash;
                });
            } // End if
        });

    $('.js-example-basic-multiple').select2();
    $('.js-example-basic-multiple2').select2();
    $('.js-example-basic-multiple3').select2();

});

function vote(value) {
    document.forms["myform"].submit();
    document.getElementById("rating").innerHTML = float_num.toFixed(value);;
  };
 // $('input[type*="radio"]').on('change', function() {
 //    var me = $(this);
 //    $(this).closest("form").submit();
 //    document.getElementById("rating").innerHTML = me.attr('value');
 //  });




