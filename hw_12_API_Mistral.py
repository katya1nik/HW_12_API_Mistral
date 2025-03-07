"""
hw_num: 12
topic: В данном задании необходимо зарегистрироваться в Mistral API по предоставленной инструкции. Получить API Ключ. Изучить документацию и на основе примеров Python кода создать три класса для взаимодействия с Mistral API
hw_theme:
  - python
  - ООП
  - Mistral API
  - ai
  - Facade
st_group: python 411
links:
---
[[13 PYTHON411 HW №13]]

# Домашнее задание 📃
**Реализация программы для работы с Mistral API с поддержкой текстовых и мультимодальных (с изображениями) запросов.**

## Краткое содержание
В данном задании необходимо зарегистрироваться в Mistral API по предоставленной инструкции. Получить API Ключ. Изучить документацию и на основе примеров Python кода создать три класса для взаимодействия с Mistral API:
- `TextRequest` – для отправки текстовых запросов;
- `ImageRequest` – для отправки запросов с изображением;
- `ChatFacade` – фасад для объединения функционала и удобного взаимодействия пользователя с системой.

Название классов и их логика может быть реализованы немного иначе. Главное, чтобы были отдельные классы на разные типы запросов, и управляющий класс.
### Технологии 🦾
- Python
- Работа с API (HTTP-запросы)
- Обработка изображений (преобразование в `Base64`)
- Принципы ООП
- Использование Git (не менее 3 коммитов)
- Скриншоты работы программы

## Задание 👷‍♂️

### Описание классов и их функциональности



1. **TextRequest**  
   Класс отвечает за отправку текстовых запросов к API Mistral.

   Методы:
   - `__init__(self, api_key: str) -> None`  
     Инициализация класса с API-ключом.
   - `send(self, text: str, model: str) -> dict`  
     Отправка текстового запроса. Метод принимает текст запроса и название модели, формирует корректный JSON для API и обрабатывает ответ.  
     
   Обработка ошибок:
   - Класс должен корректно обрабатывать ошибки соединения и ошибки API, используя механизм исключений.

2. **ImageRequest**  
   Класс предназначен для отправки запросов, включающих изображение.

   Методы:
   - `__init__(self, api_key: str) -> None`  
     Инициализация с API-ключом.
   - `send(self, text: str, image_path: str, model: str) -> dict`  
     Отправка мультимодального запроса, объединяющего текст и изображение.  
     Задачи метода:
     - Загрузка изображения по указанному пути.
     - Преобразование изображения в формат Base64.
     - Формирование корректного JSON с текстовыми данными и данными изображения.
     - Отправка запроса к API и обработка ответа.
     
   Обработка ошибок:
   - Метод должен обрабатывать ошибки загрузки файла (например, если файл не найден) и ошибки, связанные с некорректным форматом изображения или размером.

3. **ChatFacade**  
   Фасад предоставляет единый интерфейс для пользователя и управляет взаимодействием с `TextRequest` и `ImageRequest`.

   Методы:
   - `__init__(self, api_key: str) -> None`  
     Инициализация с API-ключом. Создаются экземпляры `TextRequest` и `ImageRequest`, а также инициализируется список доступных моделей.
   - `select_mode(self) -> int`  
     Предоставляет пользователю выбор типа запроса: 1 – текстовый, 2 – с изображением.
   - `select_model(self, mode: int) -> str`  
     Позволяет выбрать модель из списка, соответствующую выбранному режиму. Фасад должен отображать только подходящие модели.
   - `load_image(self, image_path: str) -> str`  
     Метод для загрузки изображения (если выбран режим с изображением). Отвечает за валидацию пути и преобразование изображения в Base64 (может делегировать эту задачу классу `ImageRequest`).
   - `ask_question(self, text: str, model: str, image_path: str = None) -> dict`  
     Основной метод для отправки запроса:
     - При выборе текстового режима – делегирует запрос методу `send` класса `TextRequest`.
     - При выборе режима с изображением – загружает изображение (или получает его через параметр) и вызывает метод `send` класса `ImageRequest`.
     - Полученный ответ сохраняется в историю переписки.
   - `get_history(self) -> list[tuple[str, dict]]`  
     Возвращает историю запросов и ответов.
   - (Дополнительно) `clear_history(self) -> None`  
     Очищает историю сообщений.

>[!info]
>#### Служебные рекомендации по работе с API запросами
>- **Текстовый запрос**: Используйте метод `send` из `TextRequest` для отправки запросов без изображений.
>- **Мультимодальный запрос**: При выборе режима работы с изображением, исправно загружайте изображение с помощью метода `load_image` и передавайте его в метод `send` класса `ImageRequest`.
>- **Фасад**: Класс `ChatFacade` должен объединять все этапы работы с API — выбор режима, модели, загрузка изображения (если требуется) и отображение истории.
  
## Таблица классов и методов

| Класс         | Файл          | Методы                                                           | Описание                                                                 | Использование                          |
| ------------- | ------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------- |
| `TextRequest` | `mistral_api.py` | `__init__(api_key: str) -> None`                                 | Инициализация с API-ключом                                               | Инициализация класса                   |
|               |               | `send(text: str, model: str) -> dict`                              | Отправка текстового запроса и обработка ответа API                       | Текстовые запросы                      |
| `ImageRequest`| `mistral_api.py` | `__init__(api_key: str) -> None`                                 | Инициализация с API-ключом                                               | Инициализация класса                   |
|               |               | `send(text: str, image_path: str, model: str) -> dict`              | Отправка запроса с изображением (текст + изображение в Base64)             | Мультимодальные запросы                |
| `ChatFacade`  | `mistral_api.py` | `__init__(api_key: str) -> None`                                 | Создание экземпляров `TextRequest` и `ImageRequest`, и инициализация модели | Фасад для взаимодействия               |
|               |               | `select_mode() -> int`                                             | Выбор типа запроса: 1 – текстовый, 2 – с изображением                      | Выбор режима                           |
|               |               | `select_model(mode: int) -> str`                                   | Выбор подходящей модели для выбранного режима                             | Выбор модели                           |
|               |               | `load_image(image_path: str) -> str`                               | Загрузка изображения и преобразование его в Base64                         | Работа с изображениями                 |
|               |               | `ask_question(text: str, model: str, image_path: str = None) -> dict` | Отправка запроса с последующим сохранением истории                         | Основной метод для пользовательского запроса |
|               |               | `get_history() -> list[tuple[str, dict]]`                          | Получение истории всех запросов и ответов                                  | Просмотр истории                       |
|               |               | `clear_history() -> None`                                          | Очистка истории запросов и ответов                                         | Управление историей                    |

## Дополнительные указания

1. **Аннотации типов и документация:**
   - Во всех классах и методах обязательно используйте аннотации типов.
   - Добавьте подробные docstring для каждого метода с описанием параметров, возвращаемых значений и возможных исключений.

2. **Работа с Git:**
   - При реализации программы необходимо сделать не менее 3 коммитов, где каждый коммит отражает логически завершённый этап работы:
     - Первый коммит – базовая структура проекта и создание классов.
     - Второй коммит – реализация функционала отправки запросов.
     - Третий коммит – интеграция фасада и реализация методов истории.

3. **Скриншоты:**
   - Помимо исходного кода, обязательно предоставьте скриншоты с успешным запуском программы и демонстрацией работы каждого режима (текстового и мультимодального запроса).

4. **Примеры использования:**
   Пример основного файла для работы с созданной системой может выглядеть следующим образом:
   ```python
   if __name__ == "__main__":
       api_key = "your_api_key_here"
       chat = ChatFacade(api_key)
       
       # Выбор режима
       mode = chat.select_mode()
       
       # Выбор модели
       model = chat.select_model(mode)
       
       # Если выбран режим с изображением, необходимо загрузить изображение
       image_path = None
       if mode == 2:
           image_path = chat.load_image("path/to/image.jpg")
       
       # Отправка запроса
       текст_вопроса = "Расскажите о последних новостях в IT."
       response = chat.ask_question(текст_вопроса, model, image_path)
       
       print("Ответ от API:", response)
       
       # Просмотр истории запросов
       print("История запросов:", chat.get_history())
   ```
   Данный пример демонстрирует последовательное выполнение всех основных шагов: выбор режима, модели, загрузку изображения (по необходимости), отправку запроса и вывод истории.

>[!warning]
>#### Критерии проверки 👌
>- **Соответствие названий классов и методов:** Названия классов и методов должны совпадать с описанными.
>- **Функциональность методов:** Каждый метод должен корректно работать с API Mistral для выбранного типа запроса.
>- **Обработка ошибок:** Реализована корректная обработка исключений при отправке запросов, загрузке изображений и работе с API.
>- **Код и Git:** Исходный код должен быть оформлен согласно стандартам PEP-8 и содержать подробные аннотации типов и docstrings. Должно быть сделано не менее 3 коммитов.
>- **Скриншоты:** Приложены скриншоты, демонстрирующие запуск программы и корректное выполнение запросов.
>- **История запросов:** Опционально. Реализован функционал сохранения и просмотра истории запросов и ответов.
"""

# # model = "mistral-large-latest"

# # client = Mistral(api_key=MISTRAL_API_KEY)

# # chat_response = client.chat.complete(
# #     model = model,
# #     messages = [
# #         {
# #             "role": "user",
# #             "content": "Кто такой Ленин?",
# #         },
# #     ]
# # )

# # print(chat_response.choices[0].message.content)


# def encode_image(image_path):
#     """Encode the image to base64."""
#     try:
#         with open(image_path, "rb") as image_file:
#             return base64.b64encode(image_file.read()).decode('utf-8')
#     except FileNotFoundError:
#         print(f"Error: The file {image_path} was not found.")
#         return None
#     except Exception as e:  # Added general exception handling
#         print(f"Error: {e}")
#         return None

# # Path to your image
# image_path = r"C:\Users\User\Desktop\photo_2024-10-06_12-03-50.jpg"

# # Getting the base64 string
# base64_image = encode_image(image_path)

# # Retrieve the API key from environment variables


# # Specify model
# model = "pixtral-12b-2409"

# # Initialize the Mistral client
# client = Mistral(api_key=MISTRAL_API_KEY)

# # Define the messages for the chat
# messages = [
#     {
#         "role": "user",
#         "content": [
#             {
#                 "type": "text",
#                 "text": "Детально опиши, что изображено на картинке.",
#             },
#             {
#                 "type": "image_url",
#                 "image_url": f"data:image/jpeg;base64,{base64_image}" 
#             }
#         ]
#     }
# ]

# # Get the chat response
# chat_response = client.chat.complete(
#     model=model,
#     messages=messages
# )

# # Print the content of the response
# print(chat_response.choices[0].message.content)

from settings import MISTRAL_API_KEY
from typing import List, Dict, Tuple, Optional
from mistralai import Mistral
import base64
class TextRequest:
    """
    Класс для отправки текстовых запросов к API Mistral."
    """
    def __init__(self, api_key: str):
       self.client = Mistral(api_key=api_key)

    def send(self, text:str, model: str) -> dict:
        """Отправляет текстовый запрос.
        """
        try:
            responce = self.client.chat.complete(
                model = model,
                messages = [
                    {
                        "role": "user",
                        "content": text,
                    },
                ]
            )
            
            return {"response": responce.choices[0].message.content}
        except Exception as e:
            return {"error": str(e)}
        

text_request = TextRequest(MISTRAL_API_KEY)
result = text_request.send("Кто такой Ленин?", "mistral-large-latest")
print("Вопрос: Кто такой Ленин?")
print("Ответ:", result["response"])





