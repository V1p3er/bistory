const dropdownToggle = document.querySelector('.dropdown-toggle');
const leftContainer = document.querySelector('.left-container');

dropdownToggle.addEventListener('click', () => {
    leftContainer.classList.toggle('show');
});