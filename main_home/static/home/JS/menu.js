let cartButtons = document.querySelectorAll('.card-button');
let card_value = document.querySelector(".added");
let pqtplus = document.querySelector(".pqt-plus");
let pqtminus = document.querySelector(".pqt-minus");
let cartvalue = 0;

cartButtons.forEach(button => {
    button.addEventListener('click', cartClick);
} );

function cartClick(){
    let button = this;
    button.classList.add('clicked');
    card_value.textContent = cartvalue += 1;
}