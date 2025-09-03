import os
import telebot

# Pobieramy token z Rendera (zmienna środowiskowa)
TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Cześć! 🤖 Twój bot działa poprawnie.")

@bot.message_handler(commands=['test'])
def test_command(message):
    bot.reply_to(message, "✅ Bot odpowiada, wszystko gra!")

bot.polling(none_stop=True)
