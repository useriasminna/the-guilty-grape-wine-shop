// GET USER AUTHENTICATION STATUS AND TYPE
let authStatus= document.getElementById('authStatus');
let userType = document.getElementById('userType');

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
    // CALL A METHOD TO CLEAR FORM INPUTS WHEN THE MODAL IS CLOSED
    const emptyFieldsOnClassChange = (modal) => {
        if (!modal.classList.contains('show')){
            let inputs = modal.getElementsByTagName('input');
            for(let el of inputs){
                if(el.classList.contains('custom-control-input')){
                    el.checked = false;
                }
                else{
                    el.value = '';
                }
            }
            let selects = modal.getElementsByTagName('select');
            for(let el of selects){
                el.selectedIndex = 0;
            }
        }
    };
    var obAdd = new MutationObserver(() => {
        emptyFieldsOnClassChange(addModal);
    });

    obAdd.observe(addModal, {
    attributes: true,
    attributeFilter: ["class"]
    });

    // SCRIPT FOR SETTING NAV ITEM ACTIVE
    let path_info = window.location.pathname + window.location.search;
    if (path_info.includes('/products/?category=')) 
        document.getElementById('navitem-wines').classList.add('nav-item-active');
    else if (path_info == '/products/?is_deluxe=True') 
        document.getElementById('navitem-deluxe').classList.add('nav-item-active');
    else if (path_info =='/products/')
        document.getElementById('navitem-products').classList.add('nav-item-active');
    else if (path_info.includes('/manage_orders/')) 
        document.getElementById('navitem-admin').classList.add('nav-item-active');
    else if (path_info.includes('/bag/')){
        if(authStatus.innerText == 'neauthenticated'){
            document.getElementById('bagNav').getElementsByTagName('a')[0].classList.add('nav-item-active');
        }
        else{
            document.getElementById('navitem-bag').classList.add('nav-item-active');
        }
    } 
    else if (path_info.includes('/wishlist/')){
        if(authStatus.innerText == 'neauthenticated'){
            document.getElementById('wishlistNav').getElementsByTagName('a')[0].classList.add('nav-item-active');
        }
        else{
            document.getElementById('navitem-wishlist').classList.add('nav-item-active');
        }
    } 
    else if (path_info.includes('/profile/')) 
        document.getElementById('navitem-profile').classList.add('nav-item-active');
    else if (path_info.includes('/login/')) 
        document.getElementById('navitem-login').classList.add('nav-item-active');
    else if (path_info.includes('/signup/')) 
        document.getElementById('navitem-signup').classList.add('nav-item-active');
    else if (path_info == '/')
        document.getElementById('navitem-home').classList.add('nav-item-active');  
    
    // ADD SCRIPT FOR SETING IMAGE INPUT FIELD INFO TEXT
    let updateImageInput = document.getElementById('id_UPDATE-image');
    let addImageInput = document.getElementById('id_ADD-image');

    if(updateImageInput){
        updateImageInput.addEventListener('input', (e) => {
            let file = e.target.files[0];
            document.getElementById('UPDATE-image-filename').textContent = `Image will be set to: ${file.name}`;
        });
    }

    if(addImageInput){
        addImageInput.addEventListener('input', (e) => {
            let file = e.target.files[0];
            document.getElementById('ADD-image-filename').textContent = `Image will be set to: ${file.name}`;
        });
    }
});
