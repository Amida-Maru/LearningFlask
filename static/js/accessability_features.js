// Theme Colour Changer
const chk = document.getElementById('chk');

chk.addEventListener('change', () => {
	document.body.classList.toggle('dark');
});

// Accessability Window
const floating_btn = document.querySelector('.floating-btn');
const close_btn = document.querySelector('.close-btn');
const social_panel_container = document.querySelector('.social-panel-container');

floating_btn.addEventListener('click', () => {
	social_panel_container.classList.toggle('visible')
});

close_btn.addEventListener('click', () => {
	social_panel_container.classList.remove('visible')
});

//Font Size Changer
/*let buttons = document.querySelector(' .buttons')
;
let btn = buttons.querySelectorAll(' .btn');
for (var i = 0; i < btn.length; i++){
    btn[i].addEventListener('click' , function(){
        let current = document.
        getElementsByClassName('active');
        current[0].className = current[0].className.
        replace("active", "");
        this.className += " active";
})
}
*/