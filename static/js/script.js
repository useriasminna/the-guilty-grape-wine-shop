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


// SCRIPT FOR PRODUCT COUNT BUTTONS FOR ADDITION AND SUBSTRACTION TO UPDATE INPUT VALUE ON CLICK
let productCountContainers = document.getElementsByClassName('product-count');

for(let container of productCountContainers){
    let buttons = container.getElementsByTagName('button');
    for (let btn of buttons){
        btn.addEventListener('click', (e) => {
            let input = e.target.parentElement.getElementsByTagName('input')[0];
            let min = input.min;
            let max = input.max;
            if (e.target.classList.contains('substraction')){
                if(parseInt(input.value) > min){
                    input.setAttribute('value', parseInt(input.value) - 1);
                }
            }  
            else if (e.target.classList.contains('addition')){
                if(parseInt(input.value) < parseInt(max)){
                    input.setAttribute('value', parseInt(input.value) + 1);        
                }
            }    
        });
    }
    
}
