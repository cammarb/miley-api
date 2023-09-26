const hamburgerBtn = document.querySelector("#hamburger-btn");
const mobileMenu = document.querySelector(".menu");

hamburgerBtn.addEventListener('click', () => {
    if (mobileMenu.classList.contains("open")) {
        mobileMenu.classList.remove("open");
    } else {
        mobileMenu.classList.add("open");
    }
});