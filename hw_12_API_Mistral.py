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
            response = self.client.chat.complete(
                model = model,
                messages = [
                    {
                        "role": "user",
                        "content": text,
                    },
                ]
            )
            
            return {"response": response.choices[0].message.content}
        except Exception as e:
            return {"error": str(e)}
        
# text_request = TextRequest(MISTRAL_API_KEY)
# result = text_request.send("Кто такой Ленин?", "mistral-large-latest")
# print("Вопрос: Кто такой Ленин?")
# print("Ответ:", result["response"])
        
class ImageRequest:
    """
    Класс для отправки запросов с изображением к API Mistral.
    """
    def __init__(self, api_key: str):
        self.client = Mistral(api_key=api_key)

    def encode_image(self, image_path: str) -> Optional[str]:
        """Кодирует изображение в base64."""
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def send(self, text: str, image_path: str) -> dict:
       
        """Отправляет запрос с изображением."""
        print(f"Начинаю обработку изображения: {image_path}")
        
        base64_image = self.encode_image(image_path)
        if not base64_image:
            return {"error": "Не удалось закодировать изображение"}
        
        try:
            messages = [{
                "role": "user",
                "content": [
                    {"type": "text", "text": "Опиши детально, что изображено на картинке"},
                    {"type": "image_url", "image_url": f"data:image/jpeg;base64,{base64_image}"}
                ]
            }]

            response = self.client.chat.complete(
                model="pixtral-12b-2409",  # Используем модель для работы с изображениями
                messages=messages
            )
            return {"response": response.choices[0].message.content}
        except Exception as e:
            print(f"Ошибка при обработке изображения: {e}")
            return {"error": str(e)}
        
# image_request = ImageRequest(MISTRAL_API_KEY)
# image_path = r"C:\Users\User\Desktop\20200224_101333.jpg"

# result = image_request.send("Детально опиши, что изображено на картинке.", image_path=image_path)

# print(result["response"])

class ChatFasade:
    """
    Инициализация фасада для работы с API Mistral.
    """
    def __init__(self, api_key: str) -> None:
        self.text_request = TextRequest(api_key)
        self.image_request = ImageRequest(api_key)
        self.history: List[Tuple[str, dict]] = []
        self.text_models = ["mistral-large-latest"]
        self.image_model = ["pixtral-12b-2409"]

    def select_mode(self) ->int:
        """Выбор режима работы с API."""
        print("Выберите режим:\n1. Текстовый запрос\n2. Запрос с изображением")
        while True:
            try:
                mode = int(input("Введите номер режима (1 или 2): "))
                if mode in [1, 2]:
                    return mode
            except ValueError:
                pass
            print("Некорректный ввод. Пожалуйста, введите 1 или 2.")

    def select_model(self, mode: int) -> str:
        """Выбор модели для запроса."""
        models = self.text_models if mode == 1 else self.image_model
        print(f"Доступные модели: {', '.join(models)}")
        return models [0]
    

    def ask_question(self, text: str, model: str, image_path: str = None) -> dict:
        """Отправка запроса и сохранение истории."""
        try:
            if model in self.image_model:
                response = self.image_request.send(text, image_path)
                print("Запрос отправлен в режиме изображения")
            else:
                response = self.text_request.send(text, model)

            if isinstance(response, dict) and "response" in response:
                self.history.append((text, response))
                self.save_history_to_file()
                return response
            else:
                return {"response": str(response)}
                
        except Exception as e:
            error_response = {"error": f"Ошибка при обработке запроса: {str(e)}"}
            self.history.append((text, error_response))
            self.save_history_to_file() 
            return {"response": f"Ошибка при обработке запроса: {str(e)}"}
        
    
    def get_history(self) -> List[Tuple[str, dict]]:
        """Получение истории запросов и ответов."""
        return self.history
    
    def clear_history(self) -> None:
        """Очистка истории запросов и ответов."""
        self.history.clear()

    def save_history_to_file(self, filename="history.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            for question, response in self.history:
                f.write(f"Запрос: {question}\n")
                f.write(f"Ответ: {response.get('response', response.get('error'))}\n\n")
       
def main():
    chat = ChatFasade(MISTRAL_API_KEY)

    while True:
        mode = chat.select_mode()
        model = chat.select_model(mode)

        if mode == 2:
            text = "Опиши детально, что изображено на картинке"
            print("\nПример пути: C:/Users/Pictures/image.jpg")
            image_path = input("Введите полный путь к изображению: ")
            print(f"Путь получен: {image_path}")
        else:
            text = "Расскажи анекдот"
            image_path = None

        result = chat.ask_question(text, model, image_path)
        print("\nОтвет:", result.get("response", result.get("error")))


        if input("\nХотите продолжить? (y/n): ").lower() != "y":
            break

        print("\nИстория запросов и ответов:")
        for question, response in chat.get_history():
            print(f"\nЗапрос: {question}")
            print(f"Ответ: {response.get('response', response.get('error', 'Ошибка'))}")

if __name__ == "__main__":
    main()

__all__ = ['TextRequest', 'ImageRequest', 'ChatFasade']



