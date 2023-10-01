import sqlite3
import asyncio


# подключение и запрос к базе
async def run_query(query, parameters=()):
    with sqlite3.connect('../database/site.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA foreign_keys = ON")
        result = cursor.execute(query, parameters)
        conn.commit()
    return result


async def check_user_in_auth(username, password):
    with sqlite3.connect('../database/site.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM auth WHERE login=? AND password=?", (username, password))
        return cursor.fetchone() is not None


async def add_user(name, surname, password, img, phone, email, school, city):
    query_users = 'INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
    param_users = (None, name, surname, img, phone, email, school, city)
    await run_query(query_users, param_users)

    query_auth = 'INSERT INTO auth VALUES (?, ?, ?)'
    param_auth = (None, email, password)
    await run_query(query_auth, param_auth)


async def del_user():
    query = 'DELETE FROM users WHERE id_user = 1'
    await run_query(query)


# while True:
#     action = input('1. Добавить пользователя\n'
#                    '2. Удалить пользователя\n'
#                    '3. Выход\n')
#     match action:
#         case '1':
#             add_user()
#         case '2':
#             del_user()
#         case '3':
#             break
