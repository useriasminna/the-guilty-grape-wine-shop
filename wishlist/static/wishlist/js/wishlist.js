// ---------------------------SCRIPT FOR UPDATING CURRENT URL WITH SORT VALUE--------------------------------------------
let sortSelector = document.getElementById('sort-selector');
if(sortSelector)
    sortSelector.addEventListener('change', (e) =>{
        let selector = e.target;
        let currentUrl = new URL(window.location);

        let selectedVal = selector.value;
        if(selectedVal != "reset"){
            if(selectedVal == 'best_sellers'){
                let sort = selectedVal;
                currentUrl.searchParams.set("sort", sort);
                currentUrl.searchParams.delete("direction");
            }
            else{
                let sort = selectedVal.split("_")[0];
                let direction = selectedVal.split("_")[1];

                currentUrl.searchParams.set("sort", sort);
                currentUrl.searchParams.set("direction", direction);
            }

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");

            window.location.replace(currentUrl);
        }
    } );

//----------------------SCRIPT FOR STOPING CLICK EVENT PROPAGATION FROM PRODUCT CONTAINBER TO OVERLAY ADD TO BAG FORM-----------------------------------------------
let formsOverlay = document.getElementsByClassName('overlay-form');
for(let form of formsOverlay){
    form.addEventListener('click', (e) => { 
        e.stopPropagation();
    });
}

//GENERATE STARS FOR REVIEWS RATING AFTER RATE VALUE
const generateStarsContainers = document.getElementsByClassName('ratings-generated');  
for(let container of generateStarsContainers){
let rateHidden = container.previousElementSibling.value;
rateHidden = Math.ceil(parseFloat(rateHidden));


for(let i=0; i<rateHidden; i++){
    let star = document.createElement("button");
    star.textContent = '★';
    star.classList.add('star');
    star.style.color = "#590243";
    container.appendChild(star);

    }

    for(let i=0; i<5-rateHidden; i++){
    let star = document.createElement("button");
    star.textContent = '★';
    star.classList.add('star');
    star.style.color = "#80808066";
    container.appendChild(star);

    }
} 

// -------------------------SCRIPT FOR PRODUCT COUNT BUTTONS FOR ADDITION AND SUBSTRACTION TO UPDATE INPUT VALUE ON CLICK---------------------------------
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
                    input.value = parseInt(input.getAttribute('value'));
                }
            }  
            else if (e.target.classList.contains('addition')){
                if(parseInt(input.value) < parseInt(max)){
                    input.setAttribute('value', parseInt(input.value) + 1);  
                    input.value = parseInt(input.getAttribute('value'));   
                }
            }    
        });
    }     
}
