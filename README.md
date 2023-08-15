# Django Telegram Message Bot

Это проект на Django, который реализует Telegram-бота для отправки и получения сообщений. Пользователи могут регистрироваться, привязывать свои аккаунты Telegram и отправлять сообщения боту, который затем пересылает их на их аккаунты в Telegram.

## Возможности

- Регистрация и аутентификация пользователей
- Привязка аккаунтов Telegram к пользователям
- Отправка сообщений боту для пересылки

## Начало работы

Следуйте этим инструкциям, чтобы установить и запустить проект локально на своей машине.

### Предварительные требования

- Python (>=3.6)
- Django (>=3.0)
- Библиотека `python-telegram-bot`

### Установка

1. Перейдите в папку проекта
2. Установите необходимые зависимости:
   pip install -r requirements.txt
3. Примените миграции базы данных:
   python manage.py migrate
4. Запустите сервер разработки:
   python manage.py runserver

## Использование

1. Зарегистрируйте нового пользователя через API:  
   POST: https://{server_url}/api/register/  
   Data: JSON  {  
     "username":"username",  
     "password":"password",  
     "first_name":"first_name"  
   }  
   Response:  {  
     "id":"id",  
     "username":"username",  
     "password":"password",  
     "first_name":"first_name",  
     "token":"token"  
   }  
     
2. Логин:  
   POST: https://{server_url}/api/login/  
   Data: JSON  {  
     "username":"username",  
     "password":"password"  
   }
     
3. Привязка аккаунта Telegram к пользователю, отправив боту сообщение с токеном.  
   Для этого отправить боту @djangomessage_bot сообщение - токен.
     
4. Используйте API для отправки сообщений боту.  
   POST: https://{server_url}/api/send-message/  
   Data: JSON  {  
     "token":"e9ab542e",  
     "message":"Hello, World!"  
   }
     
5. Используйте API для получения списка сообщении.  
   GET: https://{server_url}/api/message-list/  
