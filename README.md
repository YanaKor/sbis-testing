# Запуск автотестов

1. Основа для написания автотестов — фреймворк pytest.

2. Склонировать этот репозиторий
> git clone https://github.com/YanaKor/sbis-testing.git

3. Установить зависимости
> pip install -r requirements.txt.

4. Команда для запуска всех тестов
> pytest .

5. Для формирования отчета в формате веб-страницы
> allure serve allure-results