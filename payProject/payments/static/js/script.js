     let url = window.location.pathname.replace("/payments/item/", "../../buy/");
    var buyButton = document.getElementById('buy-button');
    buyButton.addEventListener('click', function() {
    fetch(url, {method: 'GET'})
    .then(response => response.json())
    .then(data => {
    console.log(data) // выводим в консоль результат выполнения response.json()
                    })
//.then(session => stripe.redirectToCheckout({ sessionId: data}))
});

