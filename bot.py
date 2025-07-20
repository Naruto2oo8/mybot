import telebot
import os

TOKEN = os.getenv("8130245687:AAGZBBsnJuty9_Bfbq9gFsYUdyGReGVf7dw")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Salom, Anime bot ishga tushdi!")

bot.infinity_polling()
