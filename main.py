# import telebot
# import math
#
# bot = telebot.TeleBot('6593318840:AAHCLZQA9chZOonVjyW6oO_OaOwAt0Srz-U')
# @bot.message_handler(commands = ['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'бот, который считает факториал числа. Введите число')
#     #bot.register_next_step_handler(msg, text_up)
#
# @bot.message_handler(func=lambda message: True)
# def calculate_factorial(message):
#     try:
#         num = int(message.text)
#         if num > 1000 or num < -1000:
#             factorial = math.factorial(num)
#             factorial_str = str(factorial)[:5]
#             bot.send_message(message.chat.id, f"Факториал числа {num} равен {factorial_str}...")
#         else:
#             factorial = math.factorial(num)
#             bot.send_message(message.chat.id, f"Факториал числа {num} равен {factorial}.")
#     except ValueError:
#         bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")
#
#
# bot.polling(none_stop=True)#Постоянно выполняется