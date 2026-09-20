<<<<<<< HEAD
from chatterbot import ChatBot


bot = ChatBot("units", logic_adapters =['chatterbot.logic.UnitConversion'])

while True:
    user_text = input("Ask a question (unit conversion):")
    chatbot_response = bot.get_response(user_text)
    print(chatbot_response)
=======
from chatterbot import ChatBot


bot = ChatBot("units", logic_adapters =['chatterbot.logic.UnitConversion'])

while True:
    user_text = input("Ask a question (unit conversion):")
    chatbot_response = bot.get_response(user_text)
    print(chatbot_response)
>>>>>>> e5ef5242dcdced5f8ed6da685405a024e6d5c53f
