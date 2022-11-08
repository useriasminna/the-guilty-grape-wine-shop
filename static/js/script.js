/*jshint esversion: 6 */
document.addEventListener("DOMContentLoaded", function(event) { 

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

    if (window.location.pathname.includes('/products/')) {  
    
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
        
        // SCRIPT FOR UPDATING CURRENT URL WITH SORT VALUE
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
        if (window.location.pathname.includes('/product_details/')) {   
            let currentProduct = document.getElementById('currentProduct');
            if(currentProduct){
                let updateModal =  document.getElementById('updateProductModal' + currentProduct.value);
                let updateModalContent = updateModal.getElementsByClassName('modal-content')[0];
                let updateForm = updateModal.getElementsByTagName('form')[0];
                let country = document.getElementById('id_country');
                let region = document.getElementById('id_region');
                let grapes = document.getElementById('id_grapes');
                let style = document.getElementById('id_style');
                let food = document.getElementById('id_food_pairing');
            
                // METHOD TO CHECK IF STRING CONTAINS ONLY LETTERS, COMMAS AND SPACES
                const only_letters_comma_space_valid = (string) => {
                    return /^[a-zA-Z, ]+$/.test(string);
                };
                // METHOD TO CHECK IF STRING CONTAINS ONLY LETTERS AND SPACES
                const only_letters_space_valid = (string) => {
                    return /^[a-zA-Z ]+$/.test(string);
                };
                // METHOD TO CHECK IF STRING CONTAINS ONLY LETTERS
                const only_letters_valid = (string) => {
                    return /^[a-zA-Z]+$/.test(string);
                };
            
                // DISPLAY ERROR
                const showError = (input, message) => {
                    // get the form-field element
                    const formField = input.parentElement;
                
                    // show the error message
                    const error = formField.querySelector('small');
                    error.textContent = message;
                };
            
                // METHOD TO CHECK IF COUNTRY VALUE IS VALID
                const checkCountry = () => {
            
                    let valid = false;
            
                    const countryValue = country.value.trim();
            
                    if (!only_letters_space_valid(countryValue)) {
                        showError(country, 'Field contains characters that are not letters or spaces');
                    } else {
                        valid = true;
                    }
                    return valid;
                };
            
            
                // METHOD TO CHECK IF REGION VALUE IS VALID
                const checkRegion = () => {
            
                let valid = false;
            
                const regionValue = region.value.trim();
            
                if (!only_letters_space_valid(regionValue)) {
                    showError(region, 'Field contains characters that are not letters or spaces');
                } else {
                    valid = true;
                }
                return valid;
                };
            
            
                // METHOD TO CHECK IF GRAPES VALUE IS VALID
                const checkGrapes = () => {
            
                    let valid = false;
                
                    const grapesValue = grapes.value.trim();
                
                    if (!only_letters_comma_space_valid(grapesValue)) {
                        showError(grapes, 'Field contains characters that are not letters, commas or spaces');
                    } else {
                        valid = true;
                    }
                    return valid;
                };
            
            
                // METHOD TO CHECK IF STYLE VALUE IS VALID
                const checkStyle = () => {
            
                    let valid = false;
                
                    const styleValue = style.value.trim();
                
                    if (!only_letters_valid(styleValue)) {
                        showError(style, 'Field contains characters that are not letters');
                    } else {
                        valid = true;
                    }
                    return valid;
                };
            
            
                // METHOD TO CHECK IF FOOD VALUE IS VALID
                const checkFood = () => {
            
                    let valid = false;
                
                    const foodValue = food.value.trim();
                
                    if (!only_letters_comma_space_valid(foodValue)) {
                        showError(food, 'Field contains characters that are not letters, commas or spaces');
                    } else {
                        valid = true;
                    }
                    return valid;
                    };
            
                // METHOD TO PREVENT FORM FOR SUBMITING IF FIELDS ARE NOT VALID
                const validateUpdateModalForm = () => {
                    
                    updateForm.addEventListener('submit', (e) => {
                        let isCountryValid = checkCountry();
                        let isRegionValid = checkRegion();
                        let isGrapesValid = checkGrapes();
                        let isStyleValid = checkStyle();
                        let isFoodValid = checkFood();
                        let isFormValid = isCountryValid && isRegionValid && isGrapesValid && isStyleValid && isFoodValid;
                        if(!isFormValid){
                            e.preventDefault();
                            if (!isCountryValid)
                                updateModal.scrollTo(0, country.offsetTop);
                            else if (! isRegionValid)
                                updateModal.scrollTo(0, region.offsetTop);
                            else if (! isGrapesValid)
                                updateModal.scrollTo(0, grapes.offsetTop);
                            else if (! isStyleValid)
                                updateModal.scrollTo(0, style.offsetTop);
                            else if (! isFoodValid)
                                updateModal.scrollTo(0, food.offsetTop);
                            updateModalContent.style.border = '2px solid red';
                        }
                    });
                    
                };
                validateUpdateModalForm();
            
                // CREATE A MUTATION OBSERVER TO DETECT IF UPDATE FORM MODAL CLASSLIST HAS CHANGED
                // CALL A METHOD TO RELOAD THE PAGE WHEN MODAL IS CLOSED TO REMOVING THE FORM ERRORS
                const reloadPageOnClassChange = (modal) => {
                    if (!modal.classList.contains('show'))
                        window.location.reload();
                };
            
                var ob = new MutationObserver(() => {
                    reloadPageOnClassChange(updateModal);
                });
            
                ob.observe(updateModal, {
                attributes: true,
                attributeFilter: ["class"]
                });
            }




            // --------------------------REVIEWS SECTION----------------------------------------------------------
            
            let authStatus= document.getElementById('authStatus');
            let userType = document.getElementById('userType');
            if(authStatus.textContent == "authenticated" && userType.textContent == "client"){
                const rating = document.getElementsByClassName('rating')[0];
                const stars = rating.getElementsByTagName('button');
                var rateValue;
                if(document.querySelector('#myReview'))
                {
                rateValue = document.querySelector('#updateRateValue');        
                }
                else{
                rateValue = document.querySelector('#rateValue');
                }
                    
                const displayUpdateForm = document.querySelector('#displayUpdateForm');

                //ADD EVENT LISTENERS FOR STAR RATING BUTTONS
                stars[0].clicked = true;
                const makeHoverStarsPurple = (limit) => {
                    for(let j=0; j<=limit; j++){
                        stars[j].style.color = "#590243";
                    }
                };

                const makeNotClickedStarsGray = (i) => {
                    for(let j=0; j<=i; j++){
                        if(!stars[j].clicked)
                        stars[j].style.color = "#80808066";
                    }
                };
                
                const makeClickedStarsPurple = (i) => {
                    rateValue.value = i+1;
                    rateValue.innerHTML = i+1;
                    for(let j=0; j<=i; j++){
                        stars[j].style.color = "#590243";
                        stars[j].clicked = true;
                    }
                    if(i != stars.length-1)
                        for(let z=i+1; z<stars.length; z++){
                        stars[z].style.color = "#80808066";
                        stars[z].clicked = false;
                        }
                };
        
                for(let i=0; i<stars.length; i++){
                    stars[i].addEventListener('mouseover', (event) => {
                    event = makeHoverStarsPurple(i);
                    });
                    
                    stars[i].addEventListener('mouseleave', (event) => {
                    event = makeNotClickedStarsGray(i);
                    });

                    stars[i].addEventListener('click', (event) => {
                    event = makeClickedStarsPurple(i);
                    });

                }
            
            //ON 'UPDATE' BUTTON CLICK, DISPLAY UPDATE FORM AND FILL IT WITH EXISTING VALUES OF THE CURRENT REVIEW 
            if(displayUpdateForm)
                displayUpdateForm.addEventListener("click", () => {
                    const updateReviewForm = document.querySelector('#updateReviewForm');
                    const reviewText = document.querySelector('#reviewTextHidden');
                    const reviewTextInput = updateReviewForm.querySelector('#updateReviewText');
                    const updateRating = updateReviewForm.querySelectorAll('.rating')[0].querySelectorAll('button');
                    const updateRate = updateReviewForm.getElementsByClassName("rate")[0];
                    const formRate = updateReviewForm.querySelector('#updateRateValue');
                    const myReview = document.querySelector('#myReview');

                    myReview.style.display = "none";
                    updateReviewForm.style.display = "block";
                    displayUpdateForm.style.display = "none";

                    formRate.value = updateRate.value;
                    reviewTextInput.textContent = reviewText.value;
                    for(let i=0; i < updateRate.value; i++){
                        updateRating[i].style.color = "#590243";
                    }
                
                });
            }

            const generateStarsContainers = document.getElementsByClassName('ratings-generated');
            //GENERATE STARS FOR REVIEWS RATING AFTER RATE VALUE

            for(let container of generateStarsContainers){
            const rateHidden = container.previousElementSibling;
        
        
            for(let i=0; i<rateHidden.value; i++){
                let star = document.createElement("button");
                star.textContent = '★';
                star.classList.add('star');
                star.style.color = "#590243";
                container.appendChild(star);
            
                }
            
                for(let i=0; i<5-rateHidden.value; i++){
                let star = document.createElement("button");
                star.textContent = '★';
                star.classList.add('star');
                star.style.color = "#80808066";
                container.appendChild(star);
            
                }
            } 
    

        }
    }
});