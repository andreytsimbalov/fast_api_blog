# FastApi Blog

Тестовое ***FastApi*** приложение в формате ***блога пользователей***

___

### Порядок работы приложения

Запускаемый файл: ```app/main.py```


___

### Миграции

- Изменение моделей в ```app/db/models```
- Создание файла миграции ```alembic revision --autogenerate -m "Migration Name"```
- Обновление базы ```alembic upgrade head```
- <u>Опционально:</u> Обновление базы до конкретной версии ```alembic upgrade 32a3231000dc```


