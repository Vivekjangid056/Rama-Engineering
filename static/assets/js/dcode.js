
(function($) {
    "use strict";
    /**---------------------------------------------*
     // *---------------Loader 
    **---------------------------------------------*/ 
    $(window).on('load', function() {
        $('#status').fadeOut();
        $('#preloader').delay(350).fadeOut('slow');
        $('body').delay(350).css({
            'overflow': 'visible'
        });
    });
    /**---------------------------------------------*
     //*------------- WOW Animation 
    **---------------------------------------------**/ 
    var wow = new WOW(
        {
            boxClass:     'wow',      //*------ default
            animateClass: 'animated', //*------ default
            offset:       0,          //*------- default
            mobile:       true,       //*------ default
            live:         true        //*------ default
        }
    );
    wow.init();
    /**---------------------------------------------*
     //*------------- Theme Option
    **---------------------------------------------*/ 
   
    
    /**---------------------------------------------*
     //*------------- Search Option
    **---------------------------------------------*/ 
    $('.search-btn a').click(function(e){
        e.preventDefault();
        $('.overlay.overlay-search').addClass('open');
    });
    $('.close-search').click(function(e){
        e.preventDefault();
        $('.overlay.overlay-search').removeClass('open');
    });
    
    $(document).keydown(function(e) {
        //*-------------- ESCAPE key pressed
        if (e.keyCode === 27) {
            if ($('.overlay.overlay-search').hasClass('open')){
                $('.overlay.overlay-search').removeClass('open');
            }
        }
    });
    /**---------------------------------------------*
     //*-------------- Sticky Nav
    **---------------------------------------------*/ 
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if (scroll >= 150) {
            $("header.navbar").addClass("menu-fixed");
        }else{
            $("header.navbar").removeClass("menu-fixed");
        }
    });
    /**---------------------------------------------*
     //*-------------- Mobile Menu
    **---------------------------------------------*/
    $(window).load(function() {
        var viewportWidth = $(window).width();
        if (viewportWidth < 992) {
            $(".navbar-right").appendTo("#navigation");
            $('<span class="close-btn"></span>').prependTo("#navigation");
        }
        $(window).resize(function () {
            if (viewportWidth < 992) {
                $(".navbar-right").appendTo("#navigation");
                $('<span class="close-btn"></span>').prependTo("#navigation");
            }
        });
    });
    $('.menu-toggle-btn').click(function() {
        $(this).addClass('active');
        $('#navigation').addClass('open');
        $('body').addClass('navigation-in');
    });
    $(document).on("click","#navigation .close-btn, #navigation a",function() {
        $('.menu-toggle-btn').removeClass('active');
        $('#navigation').removeClass('open');
        $('body').removeClass('navigation-in');
    });
    $(document).keydown(function(e) {
        //*------------ ESCAPE key pressed
        if (e.keyCode === 27) {
            $('.menu-toggle-btn').removeClass('active');
            $('#navigation').removeClass('open');
            $('body').removeClass('navigation-in');
        }
    });
    jQuery('#navigation ul li.menu-item-has-children > a').after('<span class="child-link"><i class="fas fa-chevron-down"></i></span>');

    jQuery('span.child-link').click(function() {
        jQuery(this).parent().siblings('li.menu-item-has-children').find('span.child-link').removeClass('active');
        jQuery(this).parent().siblings('li.menu-item-has-children').find('ul').slideUp(350);
        jQuery(this).next('ul').slideToggle(350);
        jQuery(this).next('ul').children('li').find('ul').slideUp(350);
        jQuery(this).next('ul').children('li').find('span.child-link').removeClass('active');
        jQuery(this).toggleClass('active');
        return false;
    });
    /**---------------------------------------------*
     //*--------- Testimonial slider
    **---------------------------------------------*/ 
    $('.theme-one .testimonial-slider').slick({
        dots: false,
        arrows: true,
        infinite: true,
        speed: 600,
        slidesToShow: 1,
    });
    $('.theme-two .testimonial-slider').slick({
        dots: false,
        arrows: true,
        infinite: false,
        autoplay: true,
        autoplaySpeed: 5000,
        speed: 600,
        slidesToShow: 3,
        slidesToScroll: 1,
        responsive: [
            {
            breakpoint: 1024,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                }
            },
            {
            breakpoint: 767,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: false,
                    dots: true,
                }
            }
        ]
    });

    $('.theme-three .testimonial-slider').slick({
        dots: true,
        arrows: false,
        infinite: true,
        speed: 1000,
        autoplaySpeed: 2000,
        slidesToShow: 1,
    });
    $('.theme-four .testimonial-slider').slick({
        dots: false,
        arrows: true,
        infinite: false,
        autoplay: false,
        autoplaySpeed: 5000,
        speed: 600,
        slidesToShow: 2,
        slidesToScroll: 1,
        responsive: [
            {
            breakpoint: 991,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });
   
    /**---------------------------------------------*
     //*----------- Screen Shot slider
    **---------------------------------------------*/ 
    $('.screenshot-slider').slick({
        dots: false,
        arrows: true,
        infinite: true,
        speed: 600,
        slidesToShow: 1,
        autoplay: true,
        autoplaySpeed: 4000,
        fade: true,
        cssEase: 'linear',
    });
   
    /**---------------------------------------------*
     //*--------- Fact Counter + Text Count
    **---------------------------------------------*/ 
    if($('.counter').length){
        $('.counter').appear(function(){
            var $t = $(this),
                n = $t.find(".counter-number").attr("data-stop"),
                r = parseInt($t.find(".counter-number").attr("data-speed"), 10);
                if (!$t.hasClass("counted")) {
                $t.addClass("counted");
                $({
                    countNum: $t.find(".counter-number").text()
                }).animate({
                    countNum: n
                }, {
                    duration: r,
                    easing: "linear",
                    step: function() {
                        $t.find(".counter-number").text(Math.floor(this.countNum));
                    },
                    complete: function() {
                        $t.find(".counter-number").text(this.countNum);
                    }
                });
            }
        },{accY: 0});
    }


    })(jQuery);