from mistralai import Mistral
from settings import MISTRAL_API_KEY
from typing import List, Tuple, Dict, Optional
import base64
import os

class TextRequest:
    def __init__(self, api_key: str):
       self.client = Mistral(api_key=api_key)

    def send(self, text:str, model: str) -> dict:
        
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
    def __init__(self, api_key: str):
        self.client = Mistral(api_key=api_key)

    def encode_image(self, image_path: str) -> Optional[str]:
        
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
                model="pixtral-12b-2409",
                messages=messages
            )
            return {"response": response.choices[0].message.content}
        except Exception as e:
            print(f"Ошибка при обработке изображения: {e}")
            return {"error": str(e)}
        
            
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
                    if not image_path:
                        print("Необходимо указать путь к изображению.")
                        return {"error": "Не указан путь к изображению"}
                    response = self.image_request.send(text, image_path)
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
# Запуск
if __name__ == "__main__":
    main()
    