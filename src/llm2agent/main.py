from .model import generate_response

user_input = None
while user_input != "exit":
    user_input = input()
    print(generate_response(user_input))