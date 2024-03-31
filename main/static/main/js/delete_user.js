// Получение CSRF-токена из куки
function getCSRFToken() {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Проверка наличия CSRF-токена в куках
            if (cookie.substring(0, 'csrftoken'.length + 1) === ('csrftoken' + '=')) {
                cookieValue = decodeURIComponent(cookie.substring('csrftoken'.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.getElementById('delete-user-btn').addEventListener('click', function () {
    var fioToDelete = document.getElementById('fio').value;
    if (confirm('Вы уверены, что хотите удалить пользователя?')) {
        // Отправка AJAX-запроса с CSRF-токеном
        var xhr = new XMLHttpRequest();
        xhr.open('POST', "{% url 'delete_user' %}", true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        // Установка CSRF-токена в заголовок запроса
        xhr.setRequestHeader('X-CSRFToken', getCSRFToken());
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    // Обработка успешного ответа
                    alert('Пользователь успешно удален');
                    window.location.reload(); // Перезагрузка страницы
                } else {
                    // Обработка ошибки
                    alert('Произошла ошибка при удалении пользователя');
                }
            }
        };
        xhr.send('fio=' + encodeURIComponent(fioToDelete));
    }
});
