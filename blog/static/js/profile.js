fetch('http://127.0.0.1:8000/api/user', {
    method: 'GET',
    headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${localStorage.getItem('access_token')}` },
}
).then(response => {
    return response.json();
})
    .then(data => {
        document.getElementById('name').textContent = 'Имя пользователя: ' + data.username
        document.getElementById('date_registration').textContent = "Дата присоединения: " + data.date_joined.substring(0, 10)
        document.getElementById('email').textContent = "Электронная почта: " + data.email
    })
    .catch(error => {

    });

function logoutFunc() {
    localStorage.removeItem('access_token');
    window.location.replace("http://127.0.0.1:8000/");
}