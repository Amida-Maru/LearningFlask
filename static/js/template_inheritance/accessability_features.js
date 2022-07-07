$(document).ready(function(){

    $('#small').click(function(e){
        e.preventDefault();
        $('h1').animate({ "font-size" : "30px" });
        $('h2').animate({ "font-size" : "16px" });
        $('h3').animate({ "font-size" : "24px" });
        $('p').animate({ "font-size" : "12px" });
        $('footer').animate({ "font-size" : "12px" });
    });

    $('#medium').click(function(e){
        e.preventDefault();
        $('h1').animate({ "font-size" : "40px" });
        $('h2').animate({ "font-size" : "20px" });
        $('h3').animate({ "font-size" : "35px" });
        $('p').animate({ "font-size" : "16px" });


        $('footer').animate({ "font-size" : "16px" });
    });

    $('#large').click(function(e){
        e.preventDefault();
        $('h1').animate({ "font-size" : "46px" });
        $('h2').animate({ "font-size" : "34px" });
        $('h3').animate({ "font-size" : "38px" });
        $('p').animate({ "font-size" : "22px" });
        $('footer').animate({ "font-size" : "22px" });
    });

    $('#max').click(function(e){
        e.preventDefault();
        $('h1').animate({ "font-size" : "50px" });
        $('h2').animate({ "font-size" : "38px" });
        $('h3').animate({ "font-size" : "40px" });
        $('p').animate({ "font-size" : "26px" , "line-height" : "26px"});
        $('footer').animate({ "font-size" : "26px" });
    });

    $("a").click(function(){
        $("a").removeClass("active");
        $(this).addClass("active");
    })

})


/*Theme Colour Changer*/
const chk = document.getElementById('chk');

chk.addEventListener('change', () => {
	document.body.classList.toggle('dark');
});


/*
const collection = document.getElementsByClassName("example");
for (let i = 0; i < collection.length; i++) {
  collection[i].style.font-size = '32px';
}
*/

