/*jshint esversion: 6 */
/*global $:false */
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

    //SCRIPT FOR SHOWING THE TOASTS
    let toasts = document.getElementsByClassName('toast');
    for(let toast of toasts){
        toast.style.display = 'block';
        toast.classList.add('show');
        let closeButton = toast.getElementsByClassName('close')[0];
        closeButton.addEventListener('click',()  => {
            toast.classList.remove('show');
            toast.style.display = 'none';
        });
    }

    // ---------------------------------------SCRIPT FOR ADDING VALIDATION TO ADD PRODUCT FORM AVAILABLE IN BASE.HTML---------------------------------------------
   
    let addModal =  document.getElementById('addProductModal');
    let addModalContent = addModal.getElementsByClassName('modal-content')[0];
    let addForm = addModal.getElementsByTagName('form')[0];
    let add_country = document.getElementById('id_ADD-country');
    let add_sku = document.getElementById('id_ADD-sku');
    let add_region = document.getElementById('id_ADD-region');
    let add_grapes = document.getElementById('id_ADD-grapes');
    let add_style = document.getElementById('id_ADD-style');
    let add_code = document.getElementById('id_ADD-code');
    let add_food = document.getElementById('id_ADD-food_pairing');


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

    // METHOD TO CHECK IF SKU IS UNIQUE
    const sku_is_not_unique = (sku) => {
        for(let product of productsData){
            if(product.fields.sku == sku)
                return true;
        }
    };

    // METHOD TO CHECK IF code IS UNIQUE
    const code_is_not_unique = (code) => {
        for(let product of productsData){
            if(product.fields.code == code)
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

    // METHOD TO CHECK IF SKU VALUE IS VALID
    const checkSku = (sku) => {

        let valid = false;

        const skuValue = sku.value.trim();

        if (sku_is_not_unique(skuValue)) {
            showError(sku, 'Sku value is already registered');
        } else {
            valid = true;
        }
        return valid;
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

    // METHOD TO CHECK IF CODE VALUE IS VALID
    const checkCode = (code) => {

        let valid = false;

        const codeValue = code.value.trim();

        if (code_is_not_unique(codeValue)) {
            showError(code, 'Code value is already registered');
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


    // METHOD TO PREVENT FORM FOR SUBMITING IF FIELDS ARE NOT VALID
    const validateAddModalForm = () => {
        
        addForm.addEventListener('submit', (e) => {
            let isSkuValid = checkSku(add_sku);
            let isCountryValid = checkCountry(add_country);
            let isRegionValid = checkRegion(add_region);
            let isGrapesValid = checkGrapes(add_grapes);
            let isStyleValid = checkStyle(add_style);
            let isCodeValid = checkCode(add_code);
            let isFoodValid = checkFood(add_food);
            let isFormValid = isCountryValid && isSkuValid && isRegionValid &&
                                isGrapesValid && isStyleValid && isCodeValid && isFoodValid;
            if(!isFormValid){
                e.preventDefault();
                if (! isSkuValid)
                    addModal.scrollTo(0, add_sku.offsetTop);
                else if (!isCountryValid)
                    addModal.scrollTo(0, add_country.offsetTop);
                else if (! isRegionValid)
                    addModal.scrollTo(0, add_region.offsetTop);
                else if (! isGrapesValid)
                    addModal.scrollTo(0, add_grapes.offsetTop);
                else if (! isStyleValid)
                    addModal.scrollTo(0, add_style.offsetTop);
                else if (! isCodeValid)
                    addModal.scrollTo(0, add_code.offsetTop);
                else if (! isFoodValid)
                    addModal.scrollTo(0, add_food.offsetTop);
                addModalContent.style.border = '2px solid red';
            }
        });
        
    };
    validateAddModalForm();

    // CREATE A MUTATION OBSERVER TO DETECT IF FORM MODAL CLASSLIST HAS CHANGED
    // CALL A METHOD TO RELOAD THE PAGE WHEN MODAL IS CLOSED TO CLEAR FORM INPUTS
    const reloadPageOnClassChange = (modal) => {
        if (!modal.classList.contains('show'))
            window.location.reload();
    };
    var obAdd = new MutationObserver(() => {
        reloadPageOnClassChange(addModal);
    });

    obAdd.observe(addModal, {
    attributes: true,
    attributeFilter: ["class"]
    });

    if (window.location.pathname == '/products/' || window.location.pathname == '/wishlist/') {  
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
    }

    if (window.location.pathname.includes('/products/') || window.location.pathname.includes('/wishlist/')) {
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

    if (window.location.pathname.includes('/products/') || window.location.pathname.includes('/wishlist/') || 
        window.location.pathname.includes('/bag/')) {
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
        }

    if (window.location.pathname.includes('/products/')) {  


        if (window.location.pathname.includes('/product_details/')) {  
            // --------------------------SCRIPT FOR ADDING VALIDATION TO UPDATE PRODUCT FORM AVAILABLE IN PRODUCT_DETAILS.HTML--------------------------------------------- 
            
            let currentProduct = document.getElementById('currentProduct');
            if(currentProduct){
                let updateModal =  document.getElementById('updateProductModal' + currentProduct.value);
                let updateModalContent = updateModal.getElementsByClassName('modal-content')[0];
                let updateForm = updateModal.getElementsByTagName('form')[0];
                let up_country = document.getElementById('id_UPDATE-country');
                let up_sku = document.getElementById('id_UPDATE-sku');
                let up_region = document.getElementById('id_UPDATE-region');
                let up_grapes = document.getElementById('id_UPDATE-grapes');
                let up_style = document.getElementById('id_UPDATE-style');
                let up_code = document.getElementById('id_UPDATE-code');
                let up_food = document.getElementById('id_UPDATE-food_pairing');

                // METHOD FOR CHECKING IF SKU IS UNIQUE EXCLUDING CURRENT SKU
                const sku_update_is_not_unique = (sku) => {
                    for(let product of productsData){
                        if(product.pk != currentProduct.value && product.fields.sku == sku)
                            return true;
                    }
                };
                
                // METHOD FOR CHECKING IF CODEE IS UNIQUE EXCLUDING CURRENT CODE
                const code_update_is_not_unique = (code) => {
                    for(let product of productsData){
                        if(product.pk != currentProduct.value && product.fields.code == code)
                            return true;
                    }
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
                                addModal.scrollTo(0, up_sku.offsetTop);
                            else if (!isCountryValid)
                                updateModal.scrollTo(0, up_country.offsetTop);
                            else if (! isRegionValid)
                                updateModal.scrollTo(0, up_region.offsetTop);
                            else if (! isGrapesValid)
                                updateModal.scrollTo(0, up_grapes.offsetTop);
                            else if (! isStyleValid)
                                updateModal.scrollTo(0, up_style.offsetTop);
                            else if (! isCodeValid)
                                addModal.scrollTo(0, up_code.offsetTop);
                            else if (! isFoodValid)
                                updateModal.scrollTo(0, up_food.offsetTop);
                            updateModalContent.style.border = '2px solid red';
                        }
                    });
                    
                };
                validateUpdateModalForm();
                
            
                // CREATE A MUTATION OBSERVER TO DETECT IF FORM MODAL CLASSLIST HAS CHANGED
                // CALL A METHOD TO RELOAD THE PAGE WHEN MODAL IS CLOSED TO CLEAR FORM INPUTS
            
                var obUpdate = new MutationObserver(() => {
                    reloadPageOnClassChange(updateModal);
                });
            
                obUpdate.observe(updateModal, {
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

        }
    }
    if (window.location.pathname == '/checkout/') {
        var stripePublicKey = document.getElementById('id_stripe_public_key').innerText.slice(1, -1);
        var clientSecret = document.getElementById('id_client_secret').innerText.slice(1, -1);
        var stripe = Stripe(stripePublicKey);
        var elements = stripe.elements();
        var style = {
            base: {
                color: '#000',
                fontSmoothing: 'antialiased',
                fontSize: '14px',
                '::placeholder': {
                    color: '#5f6468'
                },
            },
            invalid: {
                color: '#dc3545',
                iconColor: '#dc3545'
            }
        };
        var card = elements.create('card', {style: style});
        card.mount('#card-element');

        // HANDLE REALTIME VALIDATION ERRORS ON THE CARD ELEMENT
        card.addEventListener('change', function (event) {
            var errorDiv = document.getElementById('card-errors');
            if (event.error) {
                var html = `
                    <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span class=" font-size-smaller">${event.error.message}</span>
                `;
                $(errorDiv).html(html);
            } else {
                errorDiv.textContent = '';
            }
        });

        // Handle form submit
        var form = document.getElementById('payment-form');

        form.addEventListener('submit', function(ev) {
            ev.preventDefault();
            card.update({ 'disabled': true});
            $('#submit-button').attr('disabled', true);
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);

            var saveInfo = Boolean($('#id-save-info').attr('checked'));
            // From using {% csrf_token %} in the form
            var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
            var postData = {
                'csrfmiddlewaretoken': csrfToken,
                'client_secret': clientSecret,
                'save_info': saveInfo,
            };
            var url = '/checkout/cache_checkout_data/';

            $.post(url, postData).done(function () {
                stripe.confirmCardPayment(clientSecret, {
                    payment_method: {
                        card: card,
                        billing_details: {
                            name: $.trim(form.full_name.value),
                            phone: $.trim(form.phone_number.value),
                            email: $.trim(form.email.value),
                            address:{
                                line1: $.trim(form.street_address1.value),
                                line2: $.trim(form.street_address2.value),
                                city: $.trim(form.town_or_city.value),
                                country: $.trim(form.country.value),
                                state: $.trim(form.county.value),
                            }
                        }
                    },
                    shipping: {
                        name: $.trim(form.full_name.value),
                        phone: $.trim(form.phone_number.value),
                        address: {
                            line1: $.trim(form.street_address1.value),
                            line2: $.trim(form.street_address2.value),
                            city: $.trim(form.town_or_city.value),
                            country: $.trim(form.country.value),
                            postal_code: $.trim(form.postcode.value),
                            state: $.trim(form.county.value),
                        }
                    },
                }).then(function(result) {
                    if (result.error) {
                        var errorDiv = document.getElementById('card-errors');
                        var html = `
                            <span class="icon" role="alert">
                            <i class="fas fa-times"></i>
                            </span>
                            <span>${result.error.message}</span>`;
                        $(errorDiv).html(html);
                        $('#payment-form').fadeToggle(100);
                        $('#loading-overlay').fadeToggle(100);
                        card.update({ 'disabled': false});
                        $('#submit-button').attr('disabled', false);
                    } else {
                        if (result.paymentIntent.status === 'succeeded') {
                            form.submit();
                        }
                    }
                });
            }).fail(function () {
                location.reload();
            });
        }); 
    }

    // SCRIPT FOR SETTING NAV ITEM ACTIVE
    path_info = window.location.pathname + window.location.search
    if (path_info.includes('/products/?category=')) 
        document.getElementById('navitem-wines').classList.add('nav-item-active');
    else if (path_info == '/products/?is_deluxe=True') 
        document.getElementById('navitem-deluxe').classList.add('nav-item-active');
    else if (path_info.includes('/products/')) 
        document.getElementById('navitem-products').classList.add('nav-item-active');

});