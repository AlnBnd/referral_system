# referral_system
### Установка и настройка
1. Клонировать репозиторий:
```bash
git clone https://github.com/AlnBnd/referral_system.git
```
2 Установить зависимости:
```bash
pip install -r requirements.txt
```
3. Для безопасного необходимо SECRET_KEY добавить в `.env` файл, который создаётся в Django проекте. 
```
SECRET_KEY=ваш_секретный_ключ_django
```
4. Настройте базу данных и выполните миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Запустить сервер разработки:
```bash
python manage.py runserver
```
### Функционал API
1. Авторизация по номеру телефона
   
   POST /send-verification-code/{phone_number}
   
   Параметры запроса: phone_number(string)
   
    ```
      {
          "phone_number": "номер_телефона_пользователя"
      }   
     
     ```
  
    Ответ при успешном запросе:
  
    Код состояния: HTTP_200_OK
    
      ```
      {
          "verification_code": "код_авторизации_пользователя"
      }
      ```
    
    Ответ при ошибки:
  
    Код состояния: HTTP_400_BAD_REQUEST
    ```
    {
        "error": "Phone number is required"
    }
    ```
2. Ввод кода авторизации
   
     POST /verify-code/{verify-code}:
     
     Параметры запроса: verify-code(string)
    ```
      {
          "verification_code": "код_авторизации_пользователя"
      }   
     
     ```
    Ответ при успешном запросе:
    
    Код состояния: HTTP_200_OK
      
      ```
      {
          "message": "Verification successful"
      }
      ```
    
    Ответ при ошибки:
  
    Код состояния: HTTP_400_BAD_REQUEST
     ```
      {
          "error": "Invalid verification code"
      }
      ```

4. Запрос на профиль пользователя

   GET /api/profile/
   
    Ответ при успешном запросе, если инвай-код был активирован:
    
    Код состояния: HTTP_200_OK
      
      ```
      {
        "phone_number": "номер_телефона_пользователя",
        "activated_invite_code": "активированный_инвай-код",
      }
      ```
      
    Ответ при успешном запросе, если инвай-код не был активирован:
    
    Код состояния: HTTP_200_OK
      
      ```
      {
        "phone_number": "номер_телефона_пользователя"
      }
      ```
    Ответ при ошибки:
  
    Код состояния: HTTP_400_BAD_REQUEST
   ```
    {
        "error": "User is not authenticated"
    }
    ```   
6. Ввод инвайт-кода в профиле
   
    Параметры запроса: invite_code(string)
   
    POST /profile/{invite_code}:
   
    Ответ при успешной активации инвайт-кода:
    
    Код состояния: HTTP_200_OK
      
      ```
      {
          "message": "Invite code activated successfully"
      }
      ```

    Ответ при ошибки:
  
    Код состояния: HTTP_400_BAD_REQUEST
   ```
    {
        "error": "Invalid invite code"
    }
    ```   
5. Вывод списка пользователей в профиле API, которые ввели инвайт-код текущего пользователя

   GET /api/invitees/

    Ответ при успешном запросе, если список пользователей отстутствует:
    
    Код состояния: HTTP_200_OK
      
      ```
    {
        "message": "List is empty"
    }
      ```
    Ответ при успешном запросе:
    
    Код состояния: HTTP_200_OK
      
      ```
    [
        {
            "phone_number": "+79537045722"
        },
        {
            "phone_number": "+79537045721"
        }
    ]
      ```   
