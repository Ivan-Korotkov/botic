import os
import sys
from telethon import TelegramClient
from telethon import utils, events
import asyncio

api_id = '3469527'
session_name = 'anon'
api_hash = '72e1d209f753433faeea2fb68da3b1fd'


async def main():
    os.chdir(sys.path[0])

    if f"{session_name}.session" in os.listdir():
        os.remove(f"{session_name}.session")
    async with TelegramClient(session_name, api_id, api_hash) as client:
        await client.send_message(-484292339,
                                  "Я ожил")

        @client.on(events.NewMessage())
        async def handler_all(event):
            chat_id = event.chat_id
            sender_id = event.sender_id
            msg_id = event.id

            sender = await event.get_sender()
            name = utils.get_display_name(sender)

            chat_from = event.chat if event.chat else (await event.get_chat())
            chat_title = utils.get_display_name(chat_from)
            print(f"ID: {chat_id} {chat_title} >>  (ID: {sender_id})  {name} - (ID: {msg_id}) {event.text}")
            if chat_id == -1001192786342:
                if event.text:
                    try:
                        print(
                            f"Нужная группа ID: {chat_id} {chat_title} >>  (ID: {sender_id})  {name} - (ID: {msg_id}) {event.text}")
                        await client.send_message(-1001208991702, event.text)
                        await client.send_message(-1001179877112, event.text)
                        await client.send_message(-1001584911325, event.text)
                    except:
                        print(
                            f"Не пришло сообщение в наши группы, но я жив!")
                        await client.send_message(-484292339,
                                                  "Не пришло сообщение в наши группы,какая-то ошибка.Но я жив!")
            if chat_id == -484292339 and chat_id != sender_id:
                if event.text:
                    print(
                        f"Я жив, спасибо Ваня, что не забыл про меня!")
                    await client.send_message(-484292339, "Я жив, спасибо Ваня, что не забыл про меня!")
                else:
                    await client.send_message(-484292339,
                                              "Я жив, но ты послал мне не текстовое сообщение! Хотел меня сломать? Тебя лызгнуть или шамарнуть?")

    # await client.run_until_disconnected()


asyncio.run(main())
