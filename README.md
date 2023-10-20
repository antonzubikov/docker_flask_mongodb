### **Это REST API контракт с использованием Docker, Flask и MongoDB.**

**Для использования необходимо:**
1. **Установить Docker Engine** на вашу локальную машину (https://docs.docker.com/engine/install/);
2. **Установить все зависимости из файла "requirements.txt"** (`python pip install -r requirements.txt`);
3. **Запустить 2 контейнера с приложением на Flask и MongoDB с помощью Docker Compose** (`docker-compose up`)

После этого **к приложению можно отправлять GET, POST и PUT запросы (с телом запроса в формате JSON ("key": "value"))**. GET запрос получает данные из базы данных, POST — добавляет, а PUT — изменяет.