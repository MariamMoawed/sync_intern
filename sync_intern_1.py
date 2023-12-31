# -*- coding: utf-8 -*-
"""sync_intern_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WXxGu4LLjpwksjy_eXrr7ZGXoLPvjZXr
"""

!pip install nltk

import nltk
from nltk.chat.util import Chat, reflections

# Define the patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'how are you', ['I am good, thank you!', 'I\'m doing well, how about you?']),
    (r'(.*) your name', ['I am a chatbot created with Python!', 'You can call me Chatbot.']),
    (r'(.*) help (.*)', ['Sure, I can help you. What do you need help with?']),
    (r'quit|exit', ['Goodbye!', 'See you later!']),
]

# Create the chatbot
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Hello! I'm your chatbot. Type 'quit' or 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    if user_input.lower() in ['quit', 'exit']:
        break