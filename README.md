# Excel Processing
Приложение реализовано с помощью фреймворка FastAPI.


## Авторизация
- Login: admin
- Password: password1

При авторизации создается jwt access token и устанавливается в cookies. Время жизни токена 5 минут.

Логин, пароль, время жизни токена, алгоритм и ключ шифрования, настраиваются в .env файле.

## Запуск локально
``` bash
poetry shell
poetry update
uvicorn src.main:app --reload
```
После запуска сервера, API приложения доступно по адресу http://localhost:8000

Swagger (OpenAPI) http://localhost:8000/docs

## Запуск в docker
``` bash
docker build . -t excel_processing
docker run -d -p 8000:8000 excel_processing
```

## Загрузка и обработка файла
Так как предполагается что обработка файла может быть длительной, после загрузки файла, асинхронно запускается его обработка. Метод загрузки upload_file возвращает идентификатор файла.

Получить статус обработки файла можно с помощью метода get_processing_status и идентификатора файла.





