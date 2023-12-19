(function($) {
	'use strict';
	// Mean Menu
	$('.mean-menu').meanmenu({ 
		meanScreenWidth: "991"
	});

	// Preloader
	$(window).on('load', function() {
		$('.preloader').fadeOut();
	});

	// Nice Select JS
	$('select').niceSelect();
	
	// Header Sticky
	$(window).on('scroll', function() {
		if ($(this).scrollTop() >150){  
			$('.navbar-area').addClass("is-sticky");
		}
		else{
			$('.navbar-area').removeClass("is-sticky");
		}
	});

	//Search text from page
	// Function to search text on the webpage
function searchText() {
	// Get the search query from the input field
	var query = document.getElementById('searchInput').value;
  
	// Create a new XMLHttpRequest object
	var xhr = new XMLHttpRequest();
  
	// Define the AJAX request
	xhr.open('GET', document.location.href, true);
  
	// Set the response type
	xhr.responseType = 'document';
  
	// Handle the AJAX response
	xhr.onreadystatechange = function() {
	  if (xhr.readyState === XMLHttpRequest.DONE) {
		if (xhr.status === 200) {
		  var foundText = false;
		  var elements = xhr.response.getElementsByTagName('*');
  
		  // Loop through all elements on the webpage
		  for (var i = 0; i < elements.length; i++) {
			var element = elements[i];
  
			// Check if the element contains the search query
			if (element.innerHTML.includes(query)) {
			  foundText = true;
			  // Highlight the found text or perform any desired action
			  element.style.backgroundColor = 'yellow';
			}
		  }
  
		  // Display a message if no matching text is found
		  if (!foundText) {
			alert('Text not found on the webpage.');
		  }
		} else {
		  alert('Error: ' + xhr.status);
		}
	  }
	};
  
	// Send the AJAX request
	xhr.send();
  }
  
	  

	// Main Slider Area
	$('.hero-slider-wrap').owlCarousel({
		loop:true,
		margin:0,
		nav:false,
		mouseDrag: true,
		items:1,
		dots: true,
		autoHeight: true,
		autoplay: true,
		smartSpeed:1500,
		autoplayHoverPause: true,
		navText: [
			"<i class='flaticon-back'></i>",
			"<i class='flaticon-right'></i>",
		],
	});

	// Partners Wrap
	$('.partners-wrap').owlCarousel({ 
		loop:true,
		nav:false,
		autoplay:true,
		autoplayHoverPause: true,
		mouseDrag: true,
		margin: 0,
		center: false,
		dots: false,
		smartSpeed:1500,
		responsive:{
			0:{
				items:1,
			},
			576:{
				items:2,
			},
			768:{
				items:3,
			},
			992:{
				items:4,
			},
			1200:{
				items:4,
			}
		}
	});

	// Testimonial Wrap
	$('.testimonial-wrap').owlCarousel({
		loop:true,
		margin:30,
		nav:false,
		mouseDrag: true,
		items:1,
		dots: false,
		autoHeight: true,
		autoplay: true,
		smartSpeed:1500,
		autoplayHoverPause: true,
		center: true,
		responsive:{
			0:{
				items:1,
			},
			576:{
				items:2,
			},
			768:{
				items:2,
			},
			992:{
				items:3,
			},
			1200:{
				items:3,
			}
		}
	});

	// Team Wrap
	$('.team-wrap').owlCarousel({
		loop:true,
		margin:30,
		nav:false,
		mouseDrag: true,
		items:1,
		dots: true,
		autoHeight: true,
		autoplay: true,
		smartSpeed:1500,
		autoplayHoverPause: true,
		center: true,
		responsive:{
			0:{
				items:1,
			},
			576:{
				items:2,
			},
			768:{
				items:2,
			},
			992:{
				items:3,
			},
			1200:{
				items:3,
			}
		}
	});

	// Testimonial Wrap Two
	$('.testimonial-wrap-two').owlCarousel({
		loop:true,
		margin:30,
		nav:false,
		mouseDrag: true,
		items:1,
		dots: false,
		autoHeight: true,
		autoplay: true,
		smartSpeed:1500,
		autoplayHoverPause: true,
		responsive:{
			0:{
				items:1,
			},
			576:{
				items:1,
			},
			768:{
				items:1,
			},
			992:{
				items:2,
			},
			1200:{
				items:2,
			}
		}
	});

	// Work Wrap
	$('.work-wrap').owlCarousel({
		loop:true,
		margin:0,
		nav:false,
		mouseDrag: true,
		items:1,
		dots: false,
		autoHeight: true,
		autoplay: true,
		smartSpeed:1500,
		autoplayHoverPause: true,
		responsive:{
			0:{
				items:1,
			},
			576:{
				items:1,
			},
			768:{
				items:2,
			},
			992:{
				items:3,
			},
			1200:{
				items:5,
			}
		}
	});

	// Hero Slider Six
	$('.hero-slider-six').owlCarousel({
		loop:true,
		margin:0,
		nav:true,
		mouseDrag: true,
		items:1,
		dots: false,
		autoHeight: true,
		autoplay: true,
		smartSpeed:800,
		autoplayHoverPause: true,
		navText: [
			"<i class='bx bx-chevrons-left'></i>",
			"<i class='bx bx-chevrons-right'></i>",
		],
	});

	// Testimonial Wrap
	$('.testimonial-wrap-six').owlCarousel({
		loop:true,
		margin:0,
		nav:true,
		mouseDrag: true,
		items:1,
		dots: false,
		autoHeight: true,
		autoplay: true,
		smartSpeed:1500,
		autoplayHoverPause: true,
		navText: [
			"<i class='flaticon-left-1'></i>",
			"<i class='flaticon-right-1'></i>",
		],
	});
	
	// Odometer 
	$('.odometer').appear(function(e) {
		var odo = $(".odometer");
		odo.each(function() {
			var countNumber = $(this).attr("data-count");
			$(this).html(countNumber);
		});
	});

	// Go to Top
	// Scroll Event
	$(window).on('scroll', function(){
		var scrolled = $(window).scrollTop();
		if (scrolled > 300) $('.go-top').addClass('active');
		if (scrolled < 300) $('.go-top').removeClass('active');
	});  

	// Click Event
	$('.go-top').on('click', function() {
		$("html, body").animate({ scrollTop: "0" },  100);
	});

	// FAQ Accordion
	$('.accordion').find('.accordion-title').on('click', function(){
		// Adds Active Class
		$(this).toggleClass('active');
		// Expand or Collapse This Panel
		$(this).next().slideToggle('fast');
		// Hide The Other Panels
		$('.accordion-content').not($(this).next()).slideUp('fast');
		// Removes Active Class From Other Titles
		$('.accordion-title').not($(this)).removeClass('active');		
	});

	// Count Time 
	function makeTimer() {
		var endTime = new Date("march  30, 2021 17:00:00 PDT");			
		var endTime = (Date.parse(endTime)) / 1000;
		var now = new Date();
		var now = (Date.parse(now) / 1000);
		var timeLeft = endTime - now;
		var days = Math.floor(timeLeft / 86400); 
		var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
		var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600 )) / 60);
		var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));
		if (hours < "10") { hours = "0" + hours; }
		if (minutes < "10") { minutes = "0" + minutes; }
		if (seconds < "10") { seconds = "0" + seconds; }
		$("#days").html(days + "<span>Days</span>");
		$("#hours").html(hours + "<span>Hours</span>");
		$("#minutes").html(minutes + "<span>Minutes</span>");
		$("#seconds").html(seconds + "<span>Seconds</span>");
	}
	setInterval(function() { makeTimer(); }, 300);

	// Animation
	new WOW().init();

	// Tabs 
	$('.tab ul.tabs').addClass('active').find('> li:eq(0)').addClass('current');
	$('.tab ul.tabs li').on('click', function (g) {
		var tab = $(this).closest('.tab'), 
		index = $(this).closest('li').index();
		tab.find('ul.tabs > li').removeClass('current');
		$(this).closest('li').addClass('current');
		tab.find('.tab_content').find('div.tabs_item').not('div.tabs_item:eq(' + index + ')').slideUp();
		tab.find('.tab_content').find('div.tabs_item:eq(' + index + ')').slideDown();
		g.preventDefault();
	});
		
	// Popup Video
	$('.popup-youtube, .popup-vimeo').magnificPopup({
		disableOn: 300,
		type: 'iframe',
		mainClass: 'mfp-fade',
		removalDelay: 160,
		preloader: false,
		fixedContentPos: false,
	});

	// Subscribe form
	$(".newsletter-form").validator().on("submit", function (event) {
		if (event.isDefaultPrevented()) {
		// handle the invalid form...
			formErrorSub();
			submitMSGSub(false, "Please enter your email correctly.");
		} else {
			// everything looks good!
			event.preventDefault();
		}
	});
	function callbackFunction (resp) {
		if (resp.result === "success") {
			formSuccessSub();
		}
		else {
			formErrorSub();
		}
	}
	function formSuccessSub(){
		$(".newsletter-form")[0].reset();
		submitMSGSub(true, "Thank you for subscribing!");
		setTimeout(function() {
			$("#validator-newsletter").addClass('hide');
		}, 4000)
	}
	function formErrorSub(){
		$(".newsletter-form").addClass("animated shake");
		setTimeout(function() {
			$(".newsletter-form").removeClass("animated shake");
		}, 1000)
	}
	function submitMSGSub(valid, msg){
		if(valid){
			var msgClasses = "validation-success";
		} else {
			var msgClasses = "validation-danger";
		}
		$("#validator-newsletter").removeClass().addClass(msgClasses).text(msg);
	}
	
	// AJAX MailChimp
	$(".newsletter-form").ajaxChimp({
		url: "https://Envy Theme.us20.list-manage.com/subscribe/post?u=60e1ffe2e8a68ce1204cd39a5&amp;id=42d6d188d9", // Your url MailChimp
		callback: callbackFunction
	});
	
	// MixItUp Shorting
	try {
        var mixer = mixitup('.shorting', {
            controls: {
                toggleDefault: 'none'
            }
        });
    } catch (err) {}

	// Search Popup JS
	$('.close-btn').on('click',function() {
		$('.search-overlay').fadeOut();
		$('.search-btn').show();
		$('.close-btn').removeClass('active');
	});
	$('.search-btn').on('click',function() {
		$(this).hide();
		$('.search-overlay').fadeIn();
		$('.close-btn').addClass('active');
	});
})(jQuery);