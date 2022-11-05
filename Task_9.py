import re

contacts = {}


def main():
    while True:
        message = input("Enter command: ")
        if message == ".":
            break
        if message.lower() in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        if message.lower() == "hello":
            print("How can I help you?")
        else:
            a = parser_input(message)
            a(message) if a else print("Unknown command")


def parser_input(message):
    functions = {
        'add': name_phone,
        'change': change_phone,
        'phone': show_phone,
        'show': show_all
    }
    message = message.split()
    return functions.get(message[0].lower())


def input_error(func):
    def inner(message):
        if func.__name__ == "show_all":
            if not contacts:
                print("You didn't add any contact")
                return
        try:
            result = func(message)
        except TypeError:
            return "Error"
        return result
    return inner

@input_error
def name_phone(message):
    message = message.split()
    if len(message) < 3:
        print("Enter name and phone")
    else:
        phone = re.findall(r'\d{3}-\d{3}-\d{2}-\d{2}', message[2])
        if phone:
            contacts[message[1]] = phone[0]
        else:
            print("Input phone in ***-***-**-** format")


@input_error
def show_all(message):
    print(contacts)


@input_error
def change_phone(message):
    message = message.split()
    if len(message) < 3:
        print("Enter name and phone")
    else:
        phone = re.findall(r'\d{3}-\d{3}-\d{2}-\d{2}', message[2])
        if message[1] not in list(contacts.keys()):
            print("Add such name at first")
        else:
            if phone:
                contacts[message[1]] = phone[0]
            else:
                print("Input phone in ***-***-**-** format")


@input_error
def show_phone(message):
    message = message.split()
    if message[1] not in list(contacts.keys()):
        print("I cant find such name")
    else:
        print(contacts.get(message[1]))


if __name__ == "__main__":
    main()
