// GET USER AUTHENTICATION STATUS AND TYPE
let authStatus= document.getElementById('authStatus');
let userType = document.getElementById('userType');

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

// --------------------------SCRIPT FOR ADDING VALIDATION TO UPDATE PRODUCT FORM AVAILABLE IN PRODUCT_DETAILS.HTML--------------------------------------------- 
if(userType.textContent == "admin"){

    let currentProduct = JSON.parse(JSON.parse(document.getElementById('currentProduct').textContent))[0];

    if(currentProduct){
        let updateModal =  document.getElementById('updateProductModal' + currentProduct.pk);
        let updateModalContent = updateModal.getElementsByClassName('modal-content')[0];
        let updateForm = updateModal.getElementsByTagName('form')[0];
        let up_country = document.getElementById('id_UPDATE-country');
        let up_sku = document.getElementById('id_UPDATE-sku');
        let up_region = document.getElementById('id_UPDATE-region');
        let up_grapes = document.getElementById('id_UPDATE-grapes');
        let up_style = document.getElementById('id_UPDATE-style');
        let up_code = document.getElementById('id_UPDATE-code');
        let up_food = document.getElementById('id_UPDATE-food_pairing');

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

        // METHOD FOR CHECKING IF SKU IS UNIQUE EXCLUDING CURRENT SKU
        const sku_update_is_not_unique = (sku) => {
            for(let product of productsData){
                if(product.pk != currentProduct.pk && product.fields.sku == sku)
                    return true;
            }
        };
        
        // METHOD FOR CHECKING IF CODEE IS UNIQUE EXCLUDING CURRENT CODE
        const code_update_is_not_unique = (code) => {
            for(let product of productsData){
                if(product.pk != currentProduct.pk && product.fields.code == code)
                    return true;
            }
        };

        let productsData = JSON.parse(JSON.parse(document.getElementById('products_data').textContent));

        // DISPLAY ERROR
        const showError = (input, message) => {
            // get the form-field element
            const formField = input.parentElement.parentElement;
        
            // show the error message
            const error = formField.querySelector('small');
            error.textContent = message;
        };

        // METHOD TO CHECK IF COUNTRY VALUE IS VALID
        const checkCountry = (country) => {

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
        const checkRegion = (region) => {

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
        const checkGrapes = (grapes) => {

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
        const checkStyle = (style) => {

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
        const checkFood = (food) => {

            let valid = false;

            const foodValue = food.value.trim();

            if (!only_letters_comma_space_valid(foodValue)) {
                showError(food, 'Field contains characters that are not letters, commas or spaces');
            } else {
                valid = true;
            }
            return valid;
        };

        // METHOD TO CHECK IF SKU VALUE IS VALID FOR UPDATE FORM
        const checkUpdateSku = (sku) => {

            let valid = false;

            const skuValue = sku.value.trim();

            if (sku_update_is_not_unique(skuValue)) {
                showError(sku, 'Sku value is already registered');
            } else {
                valid = true;
            }
            return valid;
        };

        // METHOD TO CHECK IF CODE VALUE IS VALID FOR UPDATE FORM
        const checkUpdateCode = (code) => {

            let valid = false;

            const codeValue = code.value.trim();

            if (code_update_is_not_unique(codeValue)) {
                showError(code, 'Code value is already registered');
            } else {
                valid = true;
            }
            return valid;
        };

        // METHOD TO PREVENT UPDATE FORM FOR SUBMITING IF FIELDS ARE NOT VALID
        const validateUpdateModalForm = () => {
            
            updateForm.addEventListener('submit', (e) => {
                
                let isSkuValid = checkUpdateSku(up_sku);
                let isCountryValid = checkCountry(up_country);
                let isRegionValid = checkRegion(up_region);
                let isGrapesValid = checkGrapes(up_grapes);
                let isStyleValid = checkStyle(up_style);
                let isCodeValid = checkUpdateCode(up_code);
                let isFoodValid = checkFood(up_food);
                let isFormValid = isCountryValid && isSkuValid && isRegionValid &&
                                    isGrapesValid && isStyleValid && isCodeValid && isFoodValid;
                if(!isFormValid){
                    e.preventDefault();
                    if (! isSkuValid)
                        updateModal.scrollTo(0, up_sku.offsetTop);
                    else if (!isCountryValid)
                        updateModal.scrollTo(0, up_country.offsetTop);
                    else if (! isRegionValid)
                        updateModal.scrollTo(0, up_region.offsetTop);
                    else if (! isGrapesValid)
                        updateModal.scrollTo(0, up_grapes.offsetTop);
                    else if (! isStyleValid)
                        updateModal.scrollTo(0, up_style.offsetTop);
                    else if (! isCodeValid)
                        updateModal.scrollTo(0, up_code.offsetTop);
                    else if (! isFoodValid)
                        updateModal.scrollTo(0, up_food.offsetTop);
                    updateModalContent.style.border = '2px solid red';
                }
            });
            
        };
        validateUpdateModalForm();
        

        // CREATE A MUTATION OBSERVER TO DETECT IF FORM MODAL CLASSLIST HAS CHANGED
        // CALL A METHOD TO PREFILL THE FORM'S INPUT WITH CURRENT PRODUCT VALUES
        const prefillFieldsOnClassChange = (modal) => {
            if (!modal.classList.contains('show')){
                let inputs = modal.getElementsByTagName('input')
                for(let el of inputs){
                    if(el.type != 'hidden')
                        if(el.classList.contains('custom-control-input')){
                            if(currentProduct.fields.is_deluxe ){
                                el.checked = true;
                            }
                        }
                        else{
                            let name = el.name.replace('UPDATE-','');
                            if(name != 'image')
                                el.value = currentProduct.fields[name];
                        }
                    
                }
                let selects = modal.getElementsByTagName('select')
                for(let el of selects){
                    let name = el.name.replace('UPDATE-','');
                    if(name == 'category'){
                        el.selectedIndex = currentProduct.fields[name]
                    }
                    else{
                        for (let option in el.options) {
                            if (el.options[option].value == currentProduct.fields[name]){
                                el.selectedIndex =  option;
                            }
                        }
                    }
                }
            }
        };
        var obUpdate = new MutationObserver(() => {
            prefillFieldsOnClassChange(updateModal);
        });

        obUpdate.observe(updateModal, {
        attributes: true,
        attributeFilter: ["class"]
        });

    }

}


// --------------------------REVIEWS SECTION----------------------------------------------------------

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