fetch('http://127.0.0.1:8000/api/card/').then(function (response) {
    response.json().then(function (cards) {
        cards = cards['results']
        for (let i = 0; i < cards.length; i++) {
            const element = cards[i];
            console.log(element)
        }
    })
});
