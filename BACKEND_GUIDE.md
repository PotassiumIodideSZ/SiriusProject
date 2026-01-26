# Sirius Backend Guide

## Быстрый старт

### Установка и запуск

```bash
cd SiriusBackend
pipenv shell
pipenv install
python manage.py migrate
python manage.py runserver
```

### Проверка зависимостей

```bash
pipenv check
```

**Версия Python:** Проект использует Python 3.12+ (проверено в Pipfile.lock)

### Доступ к Swagger

- **Swagger UI:** http://localhost:8000/api/docs/
- **ReDoc:** http://localhost:8000/api/redoc/
- **Schema:** http://localhost:8000/api/schema/

## Тестирование для Джунов (Junior Developers)

### Запуск сервера

Сервер должен быть запущен перед тестированием:

```bash
cd SiriusBackend
pipenv shell
python manage.py runserver
```

### Проверка API через Swagger

1. Откройте http://localhost:8000/api/docs/
2. Нажмите кнопку **"Authorize"** в правом верхнем углу
3. Введите токен в формате: `Token your_auth_token`
4. Нажмите **"Authorize"**
5. Тестируйте endpoints прямо в интерфейсе

### Основные тесты

**1. Регистрация пользователя**
```bash
curl -X POST http://localhost:8000/api/auth/registration/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "first_name": "Test",
    "last_name": "User"
  }'
```

**2. Создание опроса**
```bash
curl -X POST http://localhost:8000/api/surveys/questionnaires/ \
  -H "Authorization: Token your_auth_token_here" \
  -H "Content-Type: application/json" \
  -d '{
    "question1": "Ответ на вопрос 1",
    "question2": "Ответ на вопрос 2"
  }'
```

**3. Создание рекомендации**
```bash
curl -X POST http://localhost:8000/api/recommendations/recommendations/ \
  -H "Authorization: Token your_auth_token_here" \
  -H "Content-Type: application/json" \
  -d '{
    "recommendation_text": "Рекомендация для пользователя"
  }'
```

**4. Получение списка опросов**
```bash
curl -X GET http://localhost:8000/api/surveys/questionnaires/ \
  -H "Authorization: Token your_auth_token_here"
```

### Проверка ответов

- **200 OK** - Успешный запрос
- **201 Created** - Ресурс создан
- **400 Bad Request** - Ошибка в данных запроса
- **401 Unauthorized** - Нет токена или неверный токен
- **404 Not Found** - Ресурс не найден
- **500 Server Error** - Ошибка на сервере


```bash
cd SiriusBackend
pipenv shell
pipenv install
python manage.py migrate
python manage.py runserver
```

### Проверка зависимостей

```bash
pipenv check
```

### Доступ к Swagger

- **Swagger UI:** http://localhost:8000/api/docs/
- **ReDoc:** http://localhost:8000/api/redoc/
- **Schema:** http://localhost:8000/api/schema/

## Обзор

Бэкенд проекта Sirius успешно модуляризован с использованием Domain-Driven Design (DDD) подхода.

## Структура проекта

```
SiriusBackend/
├── authentication/           # Модуль аутентификации
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py              # User модель
│   ├── serializers.py          # CustomRegisterSerializer, UserSerializer
│   ├── views.py               # UserViewSet с Swagger документацией
│   ├── urls.py                # API endpoints для пользователей
│   └── admin.py               # Админка для пользователей
├── surveys/                 # Модуль опросов
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py              # Questionnaire модель
│   ├── serializers.py          # QuestionnaireSerializer
│   ├── views.py               # QuestionnaireViewSet с Swagger документацией
│   ├── urls.py                # API endpoints для опросов
│   └── admin.py               # Админка для опросов
├── recommendations/         # Модуль рекомендаций
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py              # Recommendation модель
│   ├── serializers.py          # RecommendationSerializer
│   ├── views.py               # RecommendationViewSet с Swagger документацией
│   ├── urls.py                # API endpoints для рекомендаций
│   └── admin.py               # Админка для рекомендаций
├── MainApp/                 # Пустое приложение (можно удалить если не используется)
├── SiriusMain/              # Конфигурация проекта
│   ├── settings.py            # Настроены drf-spectacular и новые модули
│   ├── urls.py               # Настроены Swagger URLs
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
└── db.sqlite3
```

## Модули

### Authentication Module (`authentication/`)

**Назначение:** Управление пользователями и аутентификация

**Модели:**
- `User` - Расширенная модель AbstractUser с кастомными полями

**API Endpoints:**
- `GET /api/users/` - Получить всех пользователей (только текущий пользователь)
- `GET /api/users/{id}/` - Получить пользователя по ID
- `POST /api/auth/registration/` - Регистрация нового пользователя
- `POST /api/auth/login/` - Вход в систему
- `POST /api/auth/logout/` - Выход из системы

**Особенности:**
- Token аутентификация
- Кастомный serializer регистрации с полями first_name и last_name
- Swagger документация для всех endpoints

### Surveys Module (`surveys/`)

**Назначение:** Управление опросами и анкетами

**Модели:**
- `Questionnaire` - Модель для хранения ответов на вопросы

**API Endpoints:**
- `GET /api/surveys/questionnaires/` - Получить все опросы текущего пользователя
- `POST /api/surveys/questionnaires/` - Создать новый опрос
- `GET /api/surveys/questionnaires/{id}/` - Получить опрос по ID
- `PUT /api/surveys/questionnaires/{id}/` - Обновить опрос
- `PATCH /api/surveys/questionnaires/{id}/` - Частично обновить опрос
- `DELETE /api/surveys/questionnaires/{id}/` - Удалить опрос

**Особенности:**
- Пользователи видят только свои опросы
- Автоматическое привязывание пользователя при создании
- Поля created_at и updated_at для отслеживания изменений

### Recommendations Module (`recommendations/`)

**Назначение:** Управление рекомендациями для пользователей

**Модели:**
- `Recommendation` - Модель для хранения рекомендаций

**API Endpoints:**
- `GET /api/recommendations/recommendations/` - Получить все рекомендации текущего пользователя
- `POST /api/recommendations/recommendations/` - Создать новую рекомендацию
- `GET /api/recommendations/recommendations/{id}/` - Получить рекомендацию по ID
- `PUT /api/recommendations/recommendations/{id}/` - Обновить рекомендацию
- `PATCH /api/recommendations/recommendations/{id}/` - Частично обновить рекомендацию
- `DELETE /api/recommendations/recommendations/{id}/` - Удалить рекомендацию

**Особенности:**
- Пользователи видят только свои рекомендации
- Автоматическое привязывание пользователя при создании
- Поля created_at и updated_at для отслеживания изменений

## Swagger Документация

### Доступ к документации

После запуска сервера откройте в браузере:

- **Swagger UI:** http://localhost:8000/api/docs/
  - Интерактивная документация
  - Возможность тестировать API прямо в браузере
  - Поддержка аутентификации

- **ReDoc:** http://localhost:8000/api/redoc/
  - Красивая документация
  - Удобная навигация

- **OpenAPI Schema (JSON):** http://localhost:8000/api/schema/
  - Схема API в формате JSON
  - Может использоваться для генерации клиентского кода

### Использование Swagger UI

1. Откройте http://localhost:8000/api/docs/
2. Нажмите кнопку **"Authorize"** в правом верхнем углу
3. Введите токен в формате: `Token your_auth_token`
4. Нажмите **"Authorize"**
5. Теперь можете тестировать все endpoints
6. Разверните любой endpoint для просмотра деталей
7. Нажмите **"Try it out"** для тестирования

## Установка и запуск

### Требования

- Python 3.12+
- pipenv (для управления зависимостями)

### Установка зависимостей

```bash
cd SiriusBackend
pipenv install
```

### Активация виртуального окружения

```bash
cd SiriusBackend
pipenv shell
```

### Создание и применение миграций

```bash
# Создать миграции для всех модулей
python manage.py makemigrations authentication
python manage.py makemigrations surveys
python manage.py makemigrations recommendations

# Применить миграции
python manage.py migrate
```

### Запуск сервера

```bash
python manage.py runserver
```

Сервер будет доступен по адресу: http://localhost:8000/

## Аутентификация

### Регистрация пользователя

```bash
curl -X POST http://localhost:8000/api/auth/registration/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "first_name": "Test",
    "last_name": "User"
  }'
```

**Ответ:**
```json
{
  "key": "auth_token_here",
  "user": {
    "id": 1,
    "username": "testuser",
    "email": "test@example.com",
    "first_name": "Test",
    "last_name": "User"
  }
}
```

### Вход в систему

```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123"
  }'
```

**Ответ:**
```json
{
  "key": "auth_token_here"
}
```

### Использование токена

Добавьте токен в заголовки всех аутентифицированных запросов:

```bash
curl -X GET http://localhost:8000/api/users/ \
  -H "Authorization: Token your_auth_token_here"
```

## Примеры запросов

### Создать опрос

```bash
curl -X POST http://localhost:8000/api/surveys/questionnaires/ \
  -H "Authorization: Token your_auth_token_here" \
  -H "Content-Type: application/json" \
  -d '{
    "question1": "Ответ на вопрос 1",
    "question2": "Ответ на вопрос 2"
  }'
```

### Создать рекомендацию

```bash
curl -X POST http://localhost:8000/api/recommendations/recommendations/ \
  -H "Authorization: Token your_auth_token_here" \
  -H "Content-Type: application/json" \
  -d '{
    "recommendation_text": "Рекомендация для пользователя"
  }'
```

### Получить все опросы

```bash
curl -X GET http://localhost:8000/api/surveys/questionnaires/ \
  -H "Authorization: Token your_auth_token_here"
```

## Настройки

### Основные настройки (settings.py)

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'MainApp',
    'authentication',        # Модуль аутентификации
    'surveys',             # Модуль опросов
    'recommendations',     # Модуль рекомендаций
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'corsheaders',
    'drf_spectacular',      # Swagger документация
]

AUTH_USER_MODEL = 'authentication.User'  # Кастомная модель пользователя

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',  # Swagger
}

REST_AUTH = {
    'REGISTER_SERIALIZER': 'authentication.serializers.CustomRegisterSerializer',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Sirius API',
    'DESCRIPTION': 'API для Sirius проекта',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
}
```

### URL конфигурация (urls.py)

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    # Swagger/OpenAPI документация
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # API endpoints
    path('api/', include('authentication.urls')),
    path('api/surveys/', include('surveys.urls')),
    path('api/recommendations/', include('recommendations.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
]
```

## Разработка

### Добавление нового модуля

1. Создайте папку модуля в `SiriusBackend/`
2. Создайте базовые файлы:
   - `__init__.py`
   - `apps.py`
   - `models.py`
   - `serializers.py`
   - `views.py`
   - `urls.py`
   - `admin.py`
3. Добавьте модуль в `INSTALLED_APPS` в `settings.py`
4. Добавьте URL роутинг в `urls.py`
5. Создайте и примените миграции

### Добавление Swagger документации

Используйте декораторы `@extend_schema` и `@extend_schema_view`:

```python
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(summary='List all items', tags=['Items']),
    retrieve=extend_schema(summary='Get item details', tags=['Items']),
    create=extend_schema(summary='Create new item', tags=['Items']),
)
class ItemViewSet(viewsets.ModelViewSet):
    # ...
```

## Тестирование

### Запуск тестов

```bash
cd SiriusBackend
pipenv shell
python manage.py test
```

### Тестирование через Swagger

1. Откройте http://localhost:8000/api/docs/
2. Авторизуйтесь с токеном
3. Тестируйте endpoints прямо в интерфейсе

## Troubleshooting

### Ошибка: No module named 'authentication'

**Решение:** Убедитесь, что вы активировали виртуальное окружение:
```bash
cd SiriusBackend
pipenv shell
```

### Ошибка: Application labels aren't unique

**Решение:** Проверьте, что нет дубликатов имен модулей в `INSTALLED_APPS`

### Ошибка: No migrations to apply

**Решение:** Создайте и примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Ошибка: 404 Not Found

**Решение:** Проверьте, что модуль добавлен в `INSTALLED_APPS` и URL роутинг настроен

### Ошибка: 401 Unauthorized

**Решение:** Убедитесь, что токен добавлен в заголовки запросов:
```bash
-H "Authorization: Token your_token_here"
```

## Преимущества модульной архитектуры

✅ **Четкое разделение ответственности** - Каждый модуль отвечает за свою область
✅ **Легкая навигация** - Быстро найти нужный код
✅ **Масштабируемость** - Легко добавить новые модули
✅ **Swagger документация** - Автоматическая генерация из кода
✅ **Изоляция контекста** - Не теряете фокус при работе с большими данными
✅ **Простота** - Минимум файлов, понятная структура
✅ **Тестируемость** - Каждый модуль можно тестировать независимо

## Следующие шаги

1. **Добавить тесты** для каждого модуля
2. **Настроить CI/CD** для автоматического тестирования
3. **Оптимизировать производительность** при необходимости
4. **Добавить логирование** для отладки
5. **Документировать бизнес-логику** в README каждого модуля

## Полезные ссылки

- Django REST Framework: https://www.django-rest-framework.org/
- drf-spectacular: https://drf-spectacular.readthedocs.io/
- Django Documentation: https://docs.djangoproject.com/
