$(document).ready(function () {
    $('.owl-carousel-section').each(function () {
        $(this).owlCarousel({
            // Owl Carousel options and configurations
            items: 3,
            loop: true,
            dots: true,
            nav: false,
            margin: 10,
            autoplay: true,
            autoplayTimeout: 3000,
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 2
                },
                1000: {
                    items: 4
                }
            }
        });
    });
});





// Add to Cart > Get ID, Collect all button id's in JSON and retrive in JS

function addToCart(event) {
    var btnId = event.target.id;
    var inputValue = document.getElementById('quantity');
    var inputQuantity = Number(inputValue.value);
    var totalItems = JSON.parse(localStorage.getItem('cartItems')) || {};

    if (totalItems[btnId] != undefined) {
        quantity = totalItems[btnId][0] + inputQuantity
        Fname = document.getElementById('title' + btnId).innerHTML;
        totalItems[btnId] = [quantity, Fname];
    }
    else {
        quantity = inputQuantity;
        Fname = document.getElementById('title' + btnId).innerHTML;
        totalItems[btnId] = [quantity, Fname];
    }
    localStorage.setItem('cartItems', JSON.stringify(totalItems))
    console.log("The items in cart: ", totalItems)
    document.getElementById('cartTotal').innerHTML = Object.keys(totalItems).length;


}






//Function for popover cart

function showPopoverContent() {
    var totalItems = JSON.parse(localStorage.getItem('cartItems')) || {};
    var contentString = "";
    for (var item in totalItems) {
        contentString += `<span>${totalItems[item][1]}: <strong>${totalItems[item][0]}</strong></span><br>`;
        button = `<button class="mt-3" onclick="clearCart()" id="clearCart">Clear Cart Now</button><a href="/shop/checkout">Checkout</a>`;

        cartContent = contentString + button

        var popoverBodies = document.getElementsByClassName('popover-body');

        for (var i = 0; i < popoverBodies.length; i++) {
            popoverBodies[i].innerHTML = cartContent;
        }
    }

}





// Event listener to update popover content when button is clicked


function clearCart() {
    localStorage.clear();
    document.getElementById('cartTotal').innerHTML = "0";

}



// Loading the page and still getting values and keys 

window.onload = function () {
    var totalItems = JSON.parse(localStorage.getItem('cartItems')) || {};
    console.log("retreived: ", totalItems)
    document.getElementById('cartTotal').innerHTML = Object.keys(totalItems).length;
}



function loadCart() {
    var cart = JSON.parse(localStorage.getItem('cartItems'));
    console.log(cart, "heh");
    for (var item in cart) {
        var titleId = 'title' + item;
        var name = document.getElementById(titleId);
        var value = cart[item]
        console.log(name.textContent)
        console.log(value)
    }
    alert("Loaded");
}


// Alerts

