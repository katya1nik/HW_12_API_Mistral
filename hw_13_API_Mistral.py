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

            
class TextRequestStrategy(RequestStrategy):
    """
    Конкретная стратегия для текстовых запросов.
    Args:
        api_key: Ключ API Mistral для аутентификации запросов
    """
    def execute(self, text: str, model: str, history: List[Tuple[str, Dict[str, Any]]] = None, image_path: str = None) -> Dict[str, Any]:
        """
        Реализует отправку текстового запроса.
        Args:
            text: Текст запроса
            model: Название модели для обработки запроса
            history: История предыдущих запросов и ответов (опционально)
            image_path: Путь к изображению (опционально)

        Returns:
            dict: Словарь с ответом или информацией об ошибке
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
        
        
class ImageRequestStrategy(RequestStrategy):
    """
    Конкретная стратегия для запросов с изображением.
    Args:
        api_key: Ключ API Mistral для аутентификации запросов.
    """
    
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
        
    def execute(self, text: str, model: str, history: List[Tuple[str, Dict[str, Any]]] = None, image_path: str = None) -> Dict[str, Any]:
        print("Начало метода execute в ImageRequestStrategy")

        """
        Реализует отправку запроса с изображением.
        Args:
            text: Текст запроса
            model: Название модели для обработки запроса
            history: История предыдущих запросов и ответов (опционально)
            image_path: Путь к изображению 

        Returns:
            dict: Словарь с ответом или информацией об ошибке
        
        """
        
        if not image_path:
            print("Путь к изображению не указан")
            return {"error": "Путь к изображению не указан"}
       
        
        base64_image = self.encode_image(image_path)
        if not base64_image:
            print("Не удалось закодировать изображение")
            return {"error": "Не удалось закодировать изображение"}
        
        try:
            print("Формирование сообщения")
            messages = [{
                "role": "user",
                "content": [
                    {"type": "text", "text": text},
                    {"type": "image_url", "image_url": f"data:image/jpeg;base64,{base64_image}"}
                ]
            }]
            print(f"Отправка запроса к модели: {model}")
            response = self.client.chat.complete(
                model=model,  # Используем модель для работы с изображениями
                messages=messages
            )
            print("Ответ получен")
            return {"response": response.choices[0].message.content}
        except Exception as e:
            print(f"Ошибка при обработке изображения: {e}")
            return {"error": str(e)}
        

class ChatFacade:
    """
    Инициализация фасада для работы с API Mistral.
    """
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.text_strategy = TextRequestStrategy(api_key)
        self.image_strategy = ImageRequestStrategy(api_key)
        self.current_strategy = self.text_strategy
        self.history: List[Tuple[str, dict]] = []
        self.text_models = ["mistral-large-latest"]
        self.image_models = ["pixtral-12b-2409", "pixtral-12b-2409-v2"]

    def change_strategy(self, strategy_type: str) -> None:
        """
        Изменяет стратегию обработки запроса.
        Args:
            strategy: Новая стратегия для обработки запросов
        Raises:
            ValueError: Если стратегия не является экземпляром класса RequestStrategy
        """
        if strategy_type.lower() == "text":
            self.current_strategy = self.text_strategy
            print("Стратегия изменена на текстовый запрос")

        elif strategy_type.lower() == "image":
            self.current_strategy = self.image_strategy
            print("Стратегия изменена на запрос с изображением")
        else:
            raise ValueError("Неверный тип стратегии")

    def select_model(self, mode: int = None) -> str:
        """Выбор режима работы с API.
        
        Returns:
            str: Название выбранной модели
        """
        if mode is None:
            models = self.text_models if self.current_strategy == self.text_strategy else self.image_models

        else:
            models = self.text_models if mode == 1 else self.image_models
        if len(models) == 1:
            print(f"Выбранная модель: {models[0]}")
            return models[0]
        
        print ("Доступные модели:")
        for i, model in enumerate(models,1):
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
        print("Начало метода load_image")
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
            print(f"Текущая стратегия: {self.current_strategy}")
            print(f"Стратегия изображений: {self.image_strategy}")

            if self.current_strategy == self.image_strategy:
                print("Проверка изображения")
                base64_image = self.image_strategy.encode_image(image_path)
                print(f"base64_image: {base64_image is not None}")
                if base64_image is None:
                    raise Exception("Не удалось преобразовать изображение в Base64")
            print("Возвращаем путь к изображению")
            return image_path
        except FileNotFoundError:
            print("Файл не найден")
            raise FileNotFoundError(f"Файл не найден: {image_path}")
        except Exception as e:
            print(f"Ошибка в load_image: {e}")
            raise Exception(f"Ошибка при загрузке изображения: {str(e)}")
    

    def ask_question(self, text: str, model: str, image_path: str = None) -> dict:
        print("Начало метода ask_question")
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
            print(f"Текущая стратегия: {self.current_strategy}")
            print(f"Модель: {model}")
            print(f"Путь к изображению: {image_path}")

            response = self.current_strategy.execute(text, model, self.history, image_path)
            print(f"Ответ получен: {response}")
            if isinstance(response, dict) and "response" in response:
                self.history.append((text, response))
                self.save_history_to_file()
                return response
            else:
                return {"response": str(response)}
                
        except Exception as e:
            print(f"Ошибка в ask_question: {e}")
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
        print("История очищена.")

    def save_history_to_file(self, filename="history.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            for question, response in self.history:
                f.write(f"Запрос: {question}\n")
                f.write(f"Ответ: {response.get('response', response.get('error'))}\n\n")


def main():
    chat = ChatFacade(MISTRAL_API_KEY)

    while True:
        print("\nВыберите режим:")
        print("1. Текстовый запрос")
        print("2. Запрос с изображением")
        print("3. Показать историю")
        print("4. Очистить историю")
        print("5. Выйти")

        try:
            choice = int(input("Введите номер режима: "))
            if choice == 1:
                chat.change_strategy('text')
                model = chat.select_model()
                text = input("Введите текст запроса: ")
                result = chat.ask_question(text, model)
                print(f"Ответ: {result.get('response', result.get('error'))}")
            elif choice == 2:
                chat.change_strategy('image')
                model = chat.select_model()
                text = input("Введите текст запроса: ")
                if not text:
                    text = "Опиши детально это изображение"
                print('\nПример пути: C:/Users/Pictures/image.jpg')
                image_path = input("Введите путь к изображению: ")

                try:
                    print("Перед вызовом load_image")
                    image_path = chat.load_image(image_path)
                    print("После вызова load_image")
                    print("Перед вызовом ask_question")
                    result = chat.ask_question(text, model, image_path)
                    print("\nОтвет:", result.get("response", result.get("error")))
                except Exception as e:
                    print(f"Ошибка: {e}")
            elif choice == 3:
                history = chat.get_history()
                if not history:
                    print("История пуста.")
                else:
                    print("История запросов и ответов:")
                    for i, (question, response) in enumerate(history, 1):
                        print(f"\n{i}. Запрос: {question}")
                        print(f"   Ответ: {response.get('responce', response.get('error', 'Ошибка'))}")

            elif choice == 4:
                chat.clear_history()
                print("История очищена.")

            elif choice == 5:
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите снова.")

        except ValueError:
            print("Неверный выбор. Пожалуйста, введите число.")
             
if __name__ == "__main__":
    main()

__all__ = ['RequestStrategy', 'TextRequestStrategy', 'ImageRequestStrategy', 'ChatFacade']
        
