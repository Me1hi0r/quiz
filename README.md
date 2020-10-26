Приложение для проведения тестирования

1. Склонировать репозиторий
2. Перейти в каталог /quiz
3. Запустить скрипт
```bash
./setup.sh
```

4. Для отправления с почты (писем активации, для пользователя), изменить  вручную настройки в файле конфигурации Django (`quize/settings.py`). 

Сейчас работает только с гугл почтой
```
EMAIL_HOST_PASSWORD = 'your_pass'
EMAIL_HOST_USER = 'your_mail'
DEFAULT_FROM_EMAIL = 'your_mail'
```

4.1 Если гугл будет выдовать ошибку, тогда необходимо активировать настройку: <Небезопасные приложения разрешены>
По ссылке:
https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4O_rPWDBDLBmN22ye9XPJCzqO_B2UAfmhc7En0AC30uOJejwFjqw7qkJCu8XGMyLSALFVwgsEr6IclubZe5AixVfmnTRg

