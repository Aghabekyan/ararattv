$(function() {
	 /*$('.slider-for').waSlider({
	  'autoplay': true,
	  'speed': 5000,
	  'slidesToScroll': 1,
	  'marginsBtwnSlides': 20,
	  'waResponsive': true,
	  'arrows': true,
	  'dots': true,
	  'swipe': true,
	  'animation':'cssEase'
	});*/
	/*$('.fotorama').fotorama();*/
	/*$('.currency').slick({
	  slidesToShow: 1,
	  slidesToScroll: 1,
	  dots: false,
	  arrows: true,
	  centerMode: true,
	  focusOnSelect: false,
	  variableWidth: true
	});*/
	$(window).scroll(function() {
		var scrollTop = $(this).scrollTop();
		if(scrollTop > 45) {
			$('header').addClass('fixed');
			$('#to_top_btn').addClass('active');
		} else {
			$('header').removeClass('fixed');
			$('#to_top_btn').removeClass('active');
		}
	})

	$('#to_top_btn').click(function() {
		$('body').animate({scrollTop: 0}, 300);
	})
	$('.has-submenu>a').click(function() {
		$(this).toggleClass('active');
	})
	$('.has-submenu>a').blur(function() {
		console.log($('.submenu:hover').length);
		if (!($('.submenu:hover').length)) {
			$(this).removeClass('active');
		} else {
			$(this).focus();
		}
	})


	$('#haylur_slider').carouFredSel({
		auto: false,
		prev: '#prev2',
		next: '#next2',
		pagination: "#pager2",
		mousewheel: true,
		swipe: {
			onMouse: true,
			onTouch: true
		}
	});

})