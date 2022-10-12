// SCRIPT FOR NAVBAR SEARCH BOX TO BE DISPLAYED ONLY WHEN THE COLLAPSIBLE NAV IS OFF

let navbarToggler = document.getElementById('navbarToggler');
let navbarTogglerButton = document.getElementById('navbarTogglerButton');

navbarTogglerButton.addEventListener('click', () => {
    let searchElements = document.getElementsByClassName('search-bar');
    if (!navbarToggler.classList.contains('show')){
        for(let el of searchElements){
            el.style.display = 'none';
        }
    }
    else{
        setTimeout(() => {
            for(let el of searchElements){
                el.style.display = 'flex';
            }
        }, 350);
    }
});

// SCRIPT FOR SETTING PADDING TOP OF CONTENT CONTAINER TO BE EQUAL WITH HEADER HEIGHT
let headerHeight = document.getElementsByTagName('header')[0].offsetHeight;
let contentContainer = document.getElementsByClassName('content-container')[0];
contentContainer.style.paddingTop= (headerHeight - 2) + 'px';
