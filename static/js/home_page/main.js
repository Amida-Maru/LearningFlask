/*Needed to run animation on index.html*/

(function($) {
	"use strict";

	function contactFormValidation() {
	}

	/*Placeholder functions*/
	function isotopeMasonry() {

	}

/*Placeholder functions*/
	function previewPannel() {

	}

	$(window).on("load", function() {
		$(".preloader").addClass("active");
		isotopeMasonry();
		setTimeout(function () {
		    $(".preloader").addClass("done");
		}, 1500);
	});
})(jQuery);