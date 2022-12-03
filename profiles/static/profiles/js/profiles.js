let countrySelected = document.getElementById('id_default_country');
// SCRIPT FOR SETTING COUNTRY PLACEHOLDER COLOR
if(!countrySelected.value) {
    countrySelected.style.color = '#6c757d';
}
countrySelected.addEventListener('change', (e) => {
    countrySelected = e.target;
    if(!countrySelected.value) {
        countrySelected.style.color = '#6c757d';
    } else {
        countrySelected.style.color = '#000';
   }
});    

// PREVENT cOUNTRY SELECT OPENING
countrySelected.addEventListener('mousedown', (e) => {
    e.preventDefault();
    e.target.blur();
    window.focus();
});
