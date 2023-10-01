import asyncio
import json
import websockets
import database.query as q

USERS = set()


async def addUser(ws):  # функция добавления соединения с пользователем
    USERS.add(ws)


async def removeUser(ws):  # функция удаления соединения с клиентом при потере с ним соединения
    USERS.remove(ws)


async def distribution(message, ws):  # выбор действия в зависимости от запроса пользователя
    data = json.loads(message)
    print(data)
    if data['type_query'] == 'signIn':  # проверка на существование такого пользователя при входе
        if await q.check_user_in_auth(data['username'], data['password']):
            print('Отправка: authorized для', ws)
            await ws.send(json.dumps({'status': 'authorized'}))  # если есть отправляется "authorized"
        else:
            print('Отправка: failure для', ws)
            await ws.send(json.dumps({'status': 'failure'}))  # если пользователь с таким логином и паролем не найден
    elif data['type_query'] == 'signUp':  # запись нового зарегистрированного пользователя в БД
        await q.add_user(data['name'], data['surname'], data['password'], data['img'],
                         data['phone'], data['email'], data['school'], data['city'])


async def server(ws):
    await addUser(ws)
    print(f'\nClient {ws} joined.')  # сообщение о подключении нового пользователя
    print(f'Пользователи: {USERS}\n')  # выводит подключенных пользователей
    while True:
        try:
            message = await ws.recv()  # принятие сообщения
            print(f'Сообщение: {message} от {ws}')  # вывод сообщения
            await distribution(message, ws)
            # ([await user.send(message) for user in USERS])  # отправка сообщений всем пользователям
        except websockets.exceptions.ConnectionClosedOK:  # человек закрыл вкладку (соединение)
            print(f'\nClient {ws} leave.')  # сообщение о том, кто покинул сервер
            await removeUser(ws)  # удаляем из общего списка активных пользователей
            print(f'Пользователи: {USERS}\n')  # выводит список пользователей после удаления
            break


Server = websockets.serve(server, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(Server)
asyncio.get_event_loop().run_forever()
