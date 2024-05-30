// if (localStorage.getItem('access_token') === null) {
//     const menu = document.getElementById('menu')

//     const login_link = document.createElement('a')
//     login_link.href = "{% url 'blog:login'%}"
//     const btn_login = document.createElement('button')
//     btn_login.className = 'button-menu'
//     btn_login.textContent = 'Вход'

//     const registration_link = document.createElement('a')
//     registration_link.href = "{% url 'blog:registration'%}"

//     const btn_registration = document.createElement('button')
//     btn_registration.className = 'button-menu'
//     btn_registration.textContent = 'Зарегистрироваться'

//     login_link.appendChild(btn_login);
//     registration_link.appendChild(btn_registration)
//     menu.appendChild(login_link);
//     menu.appendChild(registration_link)
// }