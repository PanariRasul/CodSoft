def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define predefined rules and responses
    rules_and_responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a computer program, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
        "name": "I'm a chatbot. You can call me anything.",
        "age": "I don't have an age. I'm a program!",
        "what can you do": "I can provide information, answer questions, or just chat with you.",
        "weather": "I'm sorry, I don't have real-time information. You can check a weather website for updates.",
        "joke": "Sure, here's a joke: Why don't scientists trust atoms? Because they make up everything!",
        "favorite color": "I don't have a favorite color. I'm all about ones and zeros!",
        "thanks": "You're welcome!",
        "how to": "I can help with general information. Try asking a specific question.",
        "how it going": "It's going well, thank you! How about you?",
        "what's up": "Not much, just chatting with you. How can I assist you today?",
        "good morning": "Good morning! Hope you have a fantastic day!",
        "good afternoon": "Good afternoon! How can I help you this afternoon?",
        "good evening": "Good evening! Anything I can do for you?",
        "tell me a fact": "Sure! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "tell me a quote": "Here's a quote: 'The only way to do great work is to love what you do.' - Steve Jobs",
        "what's your favorite book": "I don't have personal preferences, but I can recommend some popular books if you're interested!",
        "how was your day": "I don't have days, but I'm here and ready to chat with you!",
        "tell me something interesting": "Sure, did you know that octopuses have three hearts and blue blood?",
        "favorite movie": "I don't watch movies, but I can help you find recommendations based on your preferences!",
        "what's for dinner": "I don't eat, but how about trying a new recipe or ordering your favorite dish?",
    }

    for rule, response in rules_and_responses.items():
        if rule in user_input:
            return response

    return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Simple chatbot loop
while True:
    
    user_input = input("You: ")


    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        print("Have A Good Day")
        break


    response = simple_chatbot(user_input)

    print("Chatbot:", response)
