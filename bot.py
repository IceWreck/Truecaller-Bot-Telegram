import telepot
import time
import requests

bot = telepot.Bot('') # Access Token. Generate with Botfather
APIToken = "" # PHPHive Truecaller API Token, Obtain it from https://tcapi.phphive.info/console/


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':

        print("text content")
        no = msg["text"]

        if no.isdigit():
            # For Searching User Details
            print("Searching for " + no)
            bot.sendMessage(chat_id, "Searching for " + no)
            contenturl = "https://tcapi.phphive.info/"+APIToken+"/search/"+no
            r = requests.get(contenturl)
            print(r.text)

            bot.sendMessage(chat_id, r.text)
            bot.sendMessage(chat_id, "Thank You.")
        else:
            print("not a number")
            bot.sendMessage(chat_id, "Please enter a valid number with country code.")

    else:
        print("not text")
        bot.sendMessage(chat_id, "Please enter a valid number with country code.")


bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
