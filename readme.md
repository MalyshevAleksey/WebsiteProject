# Прогресс:
## Сервер
__На данный момент реализованы запросы получения__:

* Логина и пароля
* Регистрация новых пользователей

Также эти запросы из БД могут отправляться клиенту. Для передачи данных используется __Websockets__, сами данные передаются 
в виде __JSON__ файлов.
## Обмен данными:
__Структура JSON (со стороны клиента):__

    let user = {
        type_query: "signIn",
        username: username,
        password: password
      };
Первая строка (___type_query___) служит для определения на сервере какое конкретно действие запрашивает клиент, данные, 
находящиеся ниже (___username, password___) - сами данные, которые необходимо обработать.

### Структура JSON (со стороны сервера):

    json.dumps({'status': 'failure'})
Пока что они примитивны, но в случае если будет необходимо передать со стороны сервера клиенту больше данных, могут 
иметь более сложный вид:

    json.dumps({
            'username': username,
            'img': img,
            'comment': comment,
            'like': count_like,
            'dislike': count_dislike,
            'date': date
    })
### Обработка JSON:
__Со стороны сервера:__

При получении JSON, его необходимо обработать с помощью команды:
    
    data = json.loads(message)
Где ___message___ - сам JSON.

После чего он будет иметь такой вид:

    {'type_query': 'signIn', 'username': 'ProstoBrotish__', 'password': 'qwerty123'}
Далее обрабатывать как ___кортеж___ (___data["type_query"]___, на выходе будет значение ___"signIn"___).

__Со стороны клиента:__

Все аналогично, только обработка с помощью команды:

    let data = JSON.parse(event.data);
Далее получение значения:

    let status = data.status

### Websockets
Для тестирования работы клиент-сервер используется ___Websockets___.
Чтобы подключиться к серверу (__локально__) необходимо указать:
__На сервере:__

    Server = websockets.serve(server, '127.0.0.1', 5678)
__У клиента:__

    const ws = new WebSocket("ws://127.0.0.1:5678/");

Также вместо __127.0.0.1__ можно указать __localhost__, но порты (в примере: __5678__) должны быть одинаковыми как на 
сервере, так и у клиента.

## Клиент:
<font size = 4>Ред. __Илхом, Мансур...__</font>
# Роли в разработке:
* __Загртдинов М.А., Курбанов И.Р.__: front-end.
* __Малышев А.А., Балясников Ф.В.__: Back-end.
* __Карпухина М.С.__: дизайнер-художник.
* __Свиридкина Н.О.__: сценарист-художник.
* __Лебедка Е.В.__: музыкальное сопровождение, аналитик.
* __Курбанов И.Р.__: тестировщик.

# Ссылки:
<font size = 5>1. [Сервер](Ссылка будет потом)</font>  
<font size = 5>2. [Клиент](Ссылка будет потом)</font>  

# Стек технологий:
## Сервер:
* Python 3.11
  * asyncio
  * json
  * websockets
  * sqlite3
* SQLite3

## Клиент:
* React
  * websocket
