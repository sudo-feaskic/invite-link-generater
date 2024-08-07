from pyrogram import Client, errors
from data import env
import uvloop # not working on Win

async def some_other_function(chat_id):
    try:
        if not os.path.exists("userbot/userbot.session"):
            return 'AUTH'
        
        else:
            uvloop.install()

            async with Client("userbot/userbot", api_id=env.api_id, api_hash=env.api_hash) as app:
                try:

                    invite_link = await app.create_chat_invite_link(chat_id, member_limit=1)
                    try:
                        await client.stop()
                    except:
                        pass
                    return str(invite_link.invite_link)

                except errors.PeerIdInvalid:
                    try:
                        try:
                            bot = await app.get_users("@bot_name") # the code get common chats by pm of the bot and then generate the link
                        except errors.UsernameNotOccupied:
                            bot = None

                        if bot:
                            payment_bot_id = bot.id
                            common_chats = await app.get_common_chats(payment_bot_id)

                            chats = [str(chat.id) for chat in common_chats]

                            if str(chat_id) in chats:
                                invite_link = await app.create_chat_invite_link(chat_id, member_limit=1)
                                return str(invite_link.invite_link)

                            else:
                                return 'Chat not found in common chats'

                        else:
                            return 'Chat bot not found'
                    except:
# this will be needed for writing data to the session (there is no way without access hash and etc. data of channel and group to get access)
                        async for dialog in app.get_dialogs(): 
                            print(f"Name: {dialog.chat.title or dialog.chat.first_name}")
                            print(f"ID: {dialog.chat.id}")
                            print(f"Type: {dialog.chat.type}")
                            print("-----")
                        await app.storage.save()
                        return await some_other_function(chat_id)

    except (errors.ApiIdInvalid, errors.SessionExpired, errors.SessionRevoked, errors.AuthKeyUnregistered) as e:
        if os.path.exists("userbot/userbot.session"):
            os.remove("userbot/userbot.session")
        return 'AUTH'
