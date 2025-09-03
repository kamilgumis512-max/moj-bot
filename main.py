import os
import telebot
import threading
import time
import random  # tylko do symulacji danych na start

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # zostaw puste na razie

bot = telebot.TeleBot(TOKEN)

# Proste komendy
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Wyświetlamy Chat ID dla łatwego kopiowania
    chat_id = message.chat.id
    bot.reply_to(message, f"Cześć! 🤖 Twój bot działa poprawnie.\nTwój Chat ID to: {chat_id}")

@bot.message_handler(commands=['test'])
def test_command(message):
    bot.reply_to(message, "✅ Bot odpowiada, wszystko gra!")

# Funkcja wysyłająca raport (tylko działa, gdy CHAT_ID już ustawione)
def send_daily_report():
    while True:
        time.sleep(24*60*60)  # czeka 24h (86400 sekund)
        if CHAT_ID is None:
            continue  # jeśli Chat ID nie jest ustawione, pomiń
        # Symulacja danych – później podłączysz realną analizę
        total_bets = random.randint(20, 30)
        won = random.randint(15, total_bets)
        lost = total_bets - won
        message = f"📊 Raport dzienny:\nŁącznie zakładów: {total_bets}\nWygrane: {won}\nPrzegrane: {lost}"
        bot.send_message(CHAT_ID, message)

# Uruchamiamy w osobnym wątku, żeby bot działał i nasłuchiwał komend
threading.Thread(target=send_daily_report, daemon=True).start()

bot.polling(none_stop=True)
