"""# Домашнее задание 📃
**Реализация паттерна "Стратегия" для работы с Mistral API.**

## Краткое содержание
В данном задании вы переработаете существующую структуру классов для работы с Mistral API, используя паттерн "Стратегия". Вы создадите абстрактный класс `RequestStrategy`, который будет определять интерфейс для всех стратегий запросов. Затем вы преобразуете существующие классы `TextRequest` и `ImageRequest` в конкретные реализации этой стратегии. Наконец, вы измените класс `ChatFacade`, чтобы он мог динамически менять стратегию во время работы программы.

### Технологии: 🦾
- Python
- Работа с API (HTTP-запросы)
- Принципы ООП
- Паттерн "Стратегия"
- Использование Git (не менее 3 коммитов)

## Задание 👷‍♂️

### Описание классов и их функциональности

1. **RequestStrategy**
   - Абстрактный класс, определяющий интерфейс для всех стратегий запросов.
   - Методы:
     - `execute(self, text: str, model: str, history: list = None, image_path: str = None) -> dict`  
       Абстрактный метод для выполнения запроса. Должен быть реализован в конкретных стратегиях.

2. **TextRequestStrategy**
   - Конкретная реализация стратегии для отправки текстовых запросов.
   - Родитель: `RequestStrategy`
   - Методы:
     - `execute(self, text: str, model: str, history: list = None, image_path: str = None) -> dict`  
       Реализует отправку текстового запроса к API Mistral.

3. **ImageRequestStrategy**
   - Конкретная реализация стратегии для отправки запросов с изображением.
   - Родитель: `RequestStrategy`
   - Методы:
     - `execute(self, text: str, model: str, history: list = None, image_path: str = None) -> dict`  
       Реализует отправку мультимодального запроса, объединяющего текст и изображение.

4. **ChatFacade**
   - Фасад предоставляет единый интерфейс для пользователя и управляет взаимодействием с `RequestStrategy`.
   - Методы:
     - `__init__(self, api_key: str) -> None`  
       Инициализация с API-ключом. Создаются экземпляры `TextRequestStrategy` и `ImageRequestStrategy`, а также инициализируется список доступных моделей.
     - `change_strategy(self, strategy_type: str) -> None`  
       Метод для смены текущей стратегии запроса. Принимает тип стратегии (`text` или `image`) и меняет текущую стратегию.
     - `select_model(self) -> str`  
       Позволяет выбрать модель из списка, соответствующую текущей стратегии.
     - `ask_question(self, text: str, model: str, image_path: str = None) -> dict`  
       Основной метод для отправки запроса. Делегирует выполнение запроса текущей стратегии.
     - `get_history(self) -> list[tuple[str, dict]]`  
       Возвращает историю запросов и ответов.
     - `clear_history(self) -> None`  
       Очищает историю сообщений.

>[!info]
>### Служебные рекомендации по работе с API запросами
>- **Текстовый запрос**: Используйте метод `execute` из `TextRequestStrategy` для отправки запросов без изображений.
>- **Мультимодальный запрос**: При выборе режима работы с изображением, используйте метод `execute` из `ImageRequestStrategy`.
>- **Фасад**: Класс `ChatFacade` должен объединять все этапы работы с API — выбор стратегии, модели, отправка запроса и отображение истории.

### Таблица классов и методов

| Класс                | Файл          | Методы                                                           | Описание                                                                 | Использование                          |
| -------------------- | ------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------- |
| `RequestStrategy`    | `mistral_api.py` | `execute(text: str, model: str, history: list = None, image_path: str = None) -> dict` | Абстрактный метод для выполнения запроса.                                | Интерфейс для стратегий                |
| `TextRequestStrategy`| `mistral_api.py` | `execute(text: str, model: str, history: list = None, image_path: str = None) -> dict` | Реализует отправку текстового запроса к API Mistral.                     | Текстовые запросы                      |
| `ImageRequestStrategy`| `mistral_api.py` | `execute(text: str, model: str, history: list = None, image_path: str = None) -> dict` | Реализует отправку запроса с изображением (текст + изображение в Base64).| Мультимодальные запросы                |
| `ChatFacade`         | `mistral_api.py` | `__init__(self, api_key: str) -> None`                                 | Создание экземпляров стратегий и инициализация модели                    | Фасад для взаимодействия               |
|                      |               | `change_strategy(self, strategy_type: str) -> None`                    | Смена текущей стратегии запроса                                          | Выбор стратегии                        |
|                      |               | `select_model(self) -> str`                                            | Выбор подходящей модели для текущей стратегии                            | Выбор модели                           |
|                      |               | `ask_question(self, text: str, model: str, image_path: str = None) -> dict` | Отправка запроса с последующим сохранением истории                         | Основной метод для пользовательского запроса |
|                      |               | `get_history(self) -> list[tuple[str, dict]]`                          | Получение истории всех запросов и ответов                                  | Просмотр истории                       |
|                      |               | `clear_history(self) -> None`                                          | Очистка истории запросов и ответов                                         | Управление историей                    |

## Дополнительные указания

1. **Аннотации типов и документация:**
   - Во всех классах и методах обязательно используйте аннотации типов.
   - Добавьте подробные docstring для каждого метода с описанием параметров, возвращаемых значений и возможных исключений.

2. **Работа с Git:**
   - При реализации программы необходимо сделать не менее 3 коммитов, где каждый коммит отражает логически завершённый этап работы:
     - Первый коммит – создание абстрактного класса и конкретных стратегий.
     - Второй коммит – реализация функционала отправки запросов.
     - Третий коммит – интеграция фасада и реализация методов истории.

3. **Примеры использования:**
   Пример основного файла для работы с созданной системой может выглядеть следующим образом:
   ```python
   if __name__ == "__main__":
       api_key = "your_api_key_here"
       chat = ChatFacade(api_key)
       
       # Смена стратегии
       chat.change_strategy("text")
       
       # Выбор модели
       model = chat.select_model()
       
       # Отправка текстового запроса
       текст_вопроса = "Расскажите о последних новостях в IT."
       response = chat.ask_question(текст_вопроса, model)
       
       print("Ответ от API:", response)
       
       # Смена стратегии на мультимодальную
       chat.change_strategy("image")
       
       # Выбор модели
       model = chat.select_model()
       
       # Отправка запроса с изображением
       image_path = "path/to/image.jpg"
       response = chat.ask_question(текст_вопроса, model, image_path)
       
       print("Ответ от API:", response)
       
       # Просмотр истории запросов
       print("История запросов:", chat.get_history())
   ```
   Данный пример демонстрирует последовательное выполнение всех основных шагов: смену стратегии, выбор модели, отправку запросов и вывод истории.

"""

from settings import MISTRAL_API_KEY
from typing import List, Dict, Tuple, Optional, Any
from mistralai import Mistral
import base64
from abc import ABC, abstractmethod


class RequestStrategy(ABC):
    '''
    Абстрактный класс для стратегий запросов.
    '''

    def  __init__(self, api_key: str):
        '''
        Инициализация стратегии с API-ключом.
        
        Args:
            api_key: Ключ API Mistral для аутентификации запросов
        '''
        self.client = Mistral(api_key=api_key)

    @abstractmethod
    def execute(self, text: str, model: str, history: List[Tuple[str, Dict[str, Any]]] = None, image_path: str = None) -> Dict[str, Any]:
        """
        Абстрактный метод для выполнения запроса.

        Args:
            text: Текст запроса
            model: Название модели для обработки запроса
            history: История предыдущих запросов и ответов (опционально)
            image_path: Путь к изображению (опционально)
                
        Returns:
            dict: Словарь с ответом или информацией об ошибке
        """
        pass

            
class TextRequestStrategy(ABC):
    """
    Класс для отправки текстовых запросов к API Mistral.
    Args:
        text: Текст запроса, который будет отправлен модели
        model: Название модели Mistral для обработки запроса
    
    Returns:
        dict: Словарь с ключом 'response', содержащим ответ модели,
              или с ключом 'error', содержащим текст ошибки
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
        
        
class ImageRequest:
    """
    Класс для отправки запросов с изображением к API Mistral.
    """
    def __init__(self, api_key: str):
        self.client = Mistral(api_key=api_key)

    def encode_image(self, image_path: str) -> Optional[str]:
        """Кодирует изображение в base64.
        Args:
            image_path: Путь к изображению
        Returns:
            Optional[str]: Строка с закодированным в base64 изображением или None в случае ошибки
        """
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def send(self, text: str, image_path: str, model: str) -> dict:
        """Отправляет запрос с изображением
        Args:
            text: Текст запроса
            image_path: Путь к изображению
            model: Название модели для обработки запроса
        
        Returns:
        dict: Словарь с ответом или ошибкой
        """
        if not image_path:
            return {"error": "Путь к изображению не указан"}
       
        
        base64_image = self.encode_image(image_path)
        if not base64_image:
            return {"error": "Не удалось закодировать изображение"}
        
        try:
            messages = [{
                "role": "user",
                "content": [
                    {"type": "text", "text": text},
                    {"type": "image_url", "image_url": f"data:image/jpeg;base64,{base64_image}"}
                ]
            }]

            response = self.client.chat.complete(
                model=model,  # Используем модель для работы с изображениями
                messages=messages
            )
            return {"response": response.choices[0].message.content}
        except Exception as e:
            print(f"Ошибка при обработке изображения: {e}")
            return {"error": str(e)}
        

class ChatFacade:
    """
    Инициализация фасада для работы с API Mistral.
    """
    def __init__(self, api_key: str) -> None:
        self.text_request = TextRequest(api_key)
        self.image_request = ImageRequest(api_key)
        self.history: List[Tuple[str, dict]] = []
        self.text_models = ["mistral-large-latest"]
        self.image_model = ["pixtral-12b-2409", "pixtral-12b-2409-v2"]

    def select_mode(self) ->int:
        """Выбор режима работы с API.
        Если доступна только одна модель для выбранного режима, она выбирается автоматически.
        Если доступно несколько моделей, пользователю предлагается выбрать одну из них.
        
        Args:
            mode: Режим работы (1 - текстовый, 2 - с изображением)
        
        Returns:
            str: Название выбранной модели
        """
        print("Выберите режим:")
        print("1. Текстовый запрос")
        print("2. Запрос с изображением")

        while True:
            print ("Ожидание ввода...")
            user_input = input("Введите номер режима: ")
            print (f'Вы ввели: {user_input}')

            if user_input == "1":
                return 1
            elif user_input == "2":
                return 2
            else:
                print("Некорректный ввод. Пожалуйста, введите 1 или 2.")
            

    def select_model(self, mode: int) -> str:
        """Выбор модели для запроса."""
        models = self.text_models if mode == 1 else self.image_model

        if len(models) == 1:
            print(f"Выбранная модель: {models[0]}")
            return models[0]
        
        print("Доступные модели:")
        for i, model in enumerate(models, 1):
            print(f"{i}. {model}")
        
        while True:
            try:
                choice = int(input("Введите номер модели: "))
                if 1 <= choice <= len(models):
                    selected_model = models[choice - 1]
                    print(f"Выбранная модель: {selected_model}")
                    return selected_model
                else:
                    print("Некорректный выбор модели. Пожалуйста, выберите номер модели из списка.")
            except ValueError:
                    print("Некорректный ввод. Пожалуйста, введите номер модели из списка.")

    def load_image(self, image_path: str) -> str:
        """Загружает изображение и преобразует его в Base64.
    
        Args:
            image_path: Путь к изображению
            
        Returns:
            str: Путь к изображению, если оно успешно загружено
            
        Raises:
            FileNotFoundError: Если файл не найден
            Exception: При других ошибках загрузки
        """
        try:
        # Пробуем открыть файл для проверки его существования
            with open(image_path, "rb") as _:
                pass

            base64_image = self.image_request.encode_image(image_path)
            if base64_image is None:
                raise Exception("Не удалось преобразовать изображение в Base64")

            return image_path
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл не найден: {image_path}")
        except Exception as e:
            raise Exception(f"Ошибка при загрузке изображения: {str(e)}")
    

    def ask_question(self, text: str, model: str, image_path: str = None) -> dict:
        """Отправка запроса и сохранение истории.
        В зависимости от выбранной модели и наличия пути к изображению,
        отправляет либо текстовый запрос, либо запрос с изображением.
        
        Args:
            text: Текст запроса
            model: Название модели для обработки запроса
            image_path: Путь к изображению (опционально, только для запросов с изображением)
        
        Returns:
            dict: Словарь с ключом 'response', содержащим ответ модели,
                или с информацией об ошибке
        """
        try:
            if model in self.image_model and image_path is not None:
              
                response = self.image_request.send(text, image_path, model)
                print("Запрос отправлен в режиме изображения")
            else:
                print("Отправка текстового запроса...")
                response = self.text_request.send(text, model)
                print("Запрос отправлен в текстовом режиме")

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
    chat = ChatFacade(MISTRAL_API_KEY)

    while True:
        mode = chat.select_mode()
        model = chat.select_model(mode)
        image_path = None

        if mode == 2:
            text = "Опиши детально, что изображено на картинке"
            print("\nПример пути: C:/Users/Pictures/image.jpg")
            image_path = input("Введите полный путь к изображению: ")
            print(f"Путь получен: {image_path}")

            try:
                image_path = chat.load_image(image_path)
                print(f"Загружено изображение: {image_path}")
            except Exception as e:
                print(f"Ошибка при загрузке изображения: {e}")
                continue
        else:
            text = input("Введите ваш вопрос: ")

        result = chat.ask_question(text, model, image_path)
        print("\nОтвет:", result.get("response", result.get("error")))

        choice = input("\nВыберите действие (c - продолжить, h - показать историю, q - выйти): ").lower()
        
        if choice == 'h':
            # Показать историю
            print("\nИстория запросов и ответов:")
            for question, response in chat.get_history():
                print(f"\nЗапрос: {question}")
                print(f"Ответ: {response.get('response', response.get('error', 'Ошибка'))}")
            
            # После показа истории спрашиваем, хочет ли пользователь продолжить
            if input("\nХотите продолжить? (y/n): ").lower() != "y":
                break
        elif choice == 'q':
            break


if __name__ == "__main__":
    main()

__all__ = ['TextRequest', 'ImageRequest', 'ChatFaсade']



