## Задание
####  1. С применением библиотеки FastAPI реализовать указанные сервисы, каждый из
#### которых реализует соответствующие методы.
#### 2. Организовать запрос через API-шлюз по адресу /client, возвращающий ответ,
#### содержащий данные в формате:
```json
{
"documents": {
... данные ответа от сервиса "личная папка" по URL /documents
},
"printers": {
... анные ответа от сервиса "печать" по URL /printers
}
}
```
#### Результат тестирования с помощью postman: 
![image](https://user-images.githubusercontent.com/43318957/200913449-830c0941-b8c6-4fd8-8f4d-f9f3e78806f3.png)