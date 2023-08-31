import telebot
import math
import threading

bot = telebot.TeleBot('6593318840:AAHCLZQA9chZOonVjyW6oO_OaOwAt0Srz-U')

# Кеш для хранения уже вычисленных факториалов
factorial_cache = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'бот, который считает факториал числа. Введите число')


def calculate_and_send_result(chat_id, num):
    try:
        # Проверяем, есть ли значение в кеше
        if num in factorial_cache:
            factorial = factorial_cache[num]
        else:
            factorial = math.factorial(num)
            factorial_cache[num] = factorial

        bot.send_message(chat_id, f"Факториал числа {num} равен {factorial}.")
    except ValueError:
        bot.send_message(chat_id, "Пожалуйста, введите корректное число.")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        num = int(message.text)
        if num > 1000 or num < -1000:
            num_str = str(num)[:5]
            bot.send_message(message.chat.id, f"Число за пределами диапазона. Первые 5 цифр: {num_str}")
        else:
            t1 = threading.Thread(target=calculate_and_send_result, args=(message.chat.id, num))
            t1.start()
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")


bot.polling(none_stop=True)
#bot.polling(none_stop=True)
#bot.polling(none_stop=True)
#bot.polling(none_stop=True)
#bot.polling(none_stop=True)
#bot.polling(none_stop=True)
#bot.polling(none_stop=True)
#bot.polling(none_stop=True)
#bot.polling(none_stop=True)
#bot.polling(none_stop=True)
#bot.polling(none_stop=True)

#bot.polling(none_stop=True)
#bot.polling(none_stop=True)
#bot.polling(none_stop=True)
#bot.polling(none_stop=True)
#bot.polling(none_stop=True)
#bot.polling(none_stop=True)
#?????????
#3333333