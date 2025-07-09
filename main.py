import telebot
from telebot import types

TOKEN = "8004664022:AAHTLTQ9A7XpghKZLhoy-s61eHZAJn5UR30"
bot = telebot.TeleBot(TOKEN)

user_db = {}


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton("Register")
    markup.add(btn1)
    bot.reply_to(
        message,
        "Hello! In this bot, you can see Club World Cup statistics of all time.\nFirst of all, you should register.",
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: message.text.lower() == "register")
def register(message):
    msg = bot.send_message(message.chat.id, "Enter your email:")
    bot.register_next_step_handler(msg, get_email)


def get_email(message):
    user_id = message.from_user.id
    email = message.text.strip()
    user_db[user_id] = {"email": email}
    msg = bot.send_message(message.chat.id, "Enter your password:")
    bot.register_next_step_handler(msg, get_password)


def get_password(message):
    user_id = message.from_user.id
    password = message.text.strip()

    if user_id in user_db:
        user_db[user_id]["password"] = password
        user_db[user_id]["registered"] = True
        bot.send_message(message.chat.id, "✅ You are successfully registered!")
    else:
        bot.send_message(message.chat.id, "⚠️ Something went wrong. Please try again by typing 'Register'.")


@bot.message_handler(func=lambda message: message.text.lower() == "statistics")
def football_statistic(message):
    user_id = message.from_user.id
    if user_id in user_db and user_db[user_id].get("registered"):
        bot.send_message(message.chat.id, "⚽ Real Madrid vs Barcelona on 21st April")
    else:
        bot.send_message(message.chat.id, "❌ Please register first by clicking 'Register'.")


if __name__ == '__main__':
    print("Bot running....")
    print(user_db)
    bot.polling(none_stop=True)
