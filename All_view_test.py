import random
import time

def greet_user():
    greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!", "Welcome!"]
    return random.choice(greetings)

def farewell_user():
    farewells = ["Goodbye!", "See you later!", "Bye!", "Take care!", "Have a great day!"]
    return random.choice(farewells)

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    responses = {
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm a chatbot created to assist you!",
        "what can you do": "I can chat with you, answer simple questions, and keep you entertained!",
        "tell me a joke": "Why don’t skeletons fight each other? Because they don’t have the guts!",
        "bye": farewell_user()
    }
    
    for key in responses:
        if key in user_input:
            return responses[key]
    
    return "I'm not sure how to respond to that."

def print_loading_message():
    print("Chatbot is thinking", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print()

def get_weather():
    weather_options = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy"]
    return f"The weather today is {random.choice(weather_options)}."

def main():
    print(greet_user())
    print("I'm your friendly chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print(farewell_user())
            break
        
        print_loading_message()
        
        if "weather" in user_input:
            response = get_weather()
        else:
            response = chatbot_response(user_input)
        
        print("Chatbot:", response)
        
if __name__ == "__main__":
    main()

def additional_function():
    data = [random.randint(1, 100) for _ in range(50)]
    sorted_data = sorted(data)
    return sorted_data

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def prime_numbers(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
        if is_prime:
            primes.append(num)
    return primes

if __name__ == "__main__":
    print("Extra Functionality Test:")
    print("Sorted Random Data:", additional_function())
    print("Factorial of 5:", factorial(5))
    print("Fibonacci Sequence (10 terms):", fibonacci(10))
    print("Prime Numbers up to 50:", prime_numbers(50))
