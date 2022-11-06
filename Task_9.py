contacts_dict = {}

def input_error(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except KeyError:
            return 'Wrong name'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'Enter name and number'
        except TypeError:
            return 'Wrong command'
    return wrapper

@input_error
def hello():
    return 'How can I help you?'

@input_error
def exit_func():
    return "Good bye"

@input_error
def name_phone(message):
    new_data = message.strip().split()
    name = new_data[0]
    phone = new_data[1]
    if name.isnumeric():
        raise ValueError('Wrong name')
    if not phone.isnumeric():
        raise ValueError('Wrong phone')
    return name, phone

@input_error
def add_name_phone(data):
    name, phone = name_phone(data)
    if name in contacts_dict:
        raise ValueError('This contact already exist.')
    contacts_dict[name] = phone
    return f'You added new contact: {name} with this {phone}.'

@input_error
def show_all():
    contacts = ''
    for key, value in contacts_dict.items():
        contacts += f'{key} : {value} \n'
    return contacts

@input_error
def change_phone(data):
    name, phone = name_phone(data)
    if name in contacts_dict:
        contacts_dict[name] = phone
        return f'You changed number to {phone} for {name}.'
    return 'Use add command'

@input_error
def show_phone(name):
    if name.strip() not in contacts_dict:
        raise ValueError('This contact does not exist.')
    return contacts_dict.get(name.strip())

functions = {
    'hello': hello,
    'add': add_name_phone,
    'change': change_phone,
    'phone': show_phone,
    'show all': show_all,
    'exit': exit_func,
    'close': exit_func,
    'good bye': exit_func
}

def parser_input(user_input):
    new_input = user_input
    data = ''
    for key in functions:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input):]
            break
    if data:
        return reaction_func(new_input)(data)
    return reaction_func(new_input)()

def reaction_func(reaction):
    return functions.get(reaction, break_func)

def break_func():
    return 'Wrong command'

def main():
    while True:
        user_input = input('Enter command: ')
        result = parser_input(user_input)
        print(result)
        if result == 'Good bye':
            break

if __name__ == "__main__":
    main()
