// drop mobile navigation
function dropNav() {
    const burger = document.getElementById('burger');
    const navDrop = document.getElementById('navDrop');
    const navLink = document.getElementById('nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    burger.addEventListener('click', () => {
        //drop nav window
        navDrop.classList.toggle('navDrop-active');

        //reveal links
        navLink.classList.toggle('nav-links-active');
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 0.2s ease forwards ${index /10}s`;
            }
        });

        //animate burger
        burger.classList.toggle('burger_X');
    });
}

// different class for active page
function activeNav() {
    var navLinks = document.querySelectorAll(".nav-item");
    var currentPage = window.location.href;

    for (i=0; i < navLinks.length; i++) {
        if (currentPage == navLinks[i].href) {
            navLinks[i].classList.toggle("nav-item-active");
        }
    }
}

const app = () => {
    dropNav();
    activeNav();
}