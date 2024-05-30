
function registrationFunc() {
    let login = document.getElementById('login').value
    let email = document.getElementById('email').value
    let password = document.getElementById('password').value

    if (login == "" || email == "" || password == "") {
        alert("Все поля должны быть заполнены!")
    }

    fetch('http://127.0.0.1:8000/api/registration/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 'username': login, 'email': email, 'password': password })
    }
    ).then(function (data) {
        console.log(data.status)
        console.log(data.json());
        // window.location.replace("http://127.0.0.1:8000/");
    })
        .catch(error => console.log('Ошибка:', error))
}

function loginFunc() {
    let login = document.getElementById('login').value
    let password = document.getElementById('password').value

    if (login == "" || password == "") {
        alert("Все поля должны быть заполнены!")
    }

    fetch('http://127.0.0.1:8000/token/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({ 'username': login, 'password': password })
    }).then(response => {
        // Проверка успешности ответа
        if (!response.ok) {
            if (response.status === 401) {
                alert('Ошибка: Неверные учетные данные.');
            } else {
                alert('Ошибка: ' + response.statusText);
            }
            throw new Error('Network response was not ok ' + response.statusText);
        }
        // Парсинг JSON-ответа
        return response.json();
    })
        .then(data => {
            const accessToken = data.access;
            localStorage.setItem('access_token', accessToken)
            window.location.replace("http://127.0.0.1:8000/");
        })
        .catch(error => {
        });
}