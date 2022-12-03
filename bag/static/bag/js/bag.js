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
