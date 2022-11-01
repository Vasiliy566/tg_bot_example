import telebot

from register import is_user_exists, create_user, add_money_to_user, get_user_balance
from utils import is_email_valid

bot = telebot.TeleBot('5714675838:AAEwGV9gqnQyI1FRlsEvtjuBqTAadrUuiFQ')


@bot.message_handler(commands=['help'])
def register(message):
    bot.send_message(message.chat.id, 'Я умею: /start /add_money /my_balance')


@bot.message_handler(commands=['start'])
def register(message):
    user_id = message.chat.id
    if is_user_exists(user_id):
        bot.send_message(user_id, 'Ты уже регистрировался!')
    else:
        bot.send_message(message.chat.id, 'Введи пожалуйста свое имя и фамилию')
        bot.register_next_step_handler(message, read_name)


def read_name(message):
    name = message.text
    bot.send_message(message.chat.id, f"Введи пожалуйста свою почту")
    bot.register_next_step_handler(message, read_email, name)


def read_email(message, name):
    email = message.text
    if is_email_valid(email):
        bot.send_message(message.chat.id, f"Спасибо за регистрацию")
        create_user(message.chat.id, name, email)
    else:
        bot.send_message(message.chat.id, f"Некорректная почта")


@bot.message_handler(commands=['add_money'])
def add_money(message):
    user_id = message.chat.id
    if not is_user_exists(user_id):
        bot.send_message(user_id, 'Сначала сделай /start и зарегистрируйся')
    else:
        bot.send_message(user_id, "Введи сумму пополнения.")
        bot.register_next_step_handler(message, read_amount)


def read_amount(message):
    user_id = message.chat.id
    try:
        money_to_add = int(message.text)
    except Exception:
        bot.send_message(user_id, "Нужно было ввести число.")
    else:
        add_money_to_user(user_id, money_to_add)
        bot.send_message(user_id, f"Ваш баланс пополнен на {money_to_add} рублей.")


@bot.message_handler(commands=['my_balance'])
def get_balance(message):
    user_id = message.chat.id
    if not is_user_exists(user_id):
        bot.send_message(user_id, 'Сначала сделай /start и зарегистрируйся')
    else:
        balance = get_user_balance(user_id)
        bot.send_message(user_id, f"Ваш баланс: {balance}")


bot.infinity_polling()
