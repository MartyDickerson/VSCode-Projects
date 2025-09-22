import nltk
import random
import string

# Download data if not already available
nltk.download("punkt")
nltk.download("wordnet")

from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi!"]],
    [r"how are you ?", ["I'm doing good, how about you?", "I'm fine, thanks for asking."]],
    [r"(.*) your name ?", ["I'm ChatBot created in Python!", "They call me PyBot."]],
    [r"quit", ["Bye! Have a great day.", "Goodbye!"]],
]

chatbot = Chat(pairs, reflections)

def start_chat():
    print("🤖 PyBot: Hi, type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()
