phone_book = []


def open_phone_book():
    with open('phone_book.txt', 'r', encoding='utf-8') as data:
        phone_book = data.readlines()
        print('Файл открыт')
        return phone_book


def save_phone_book():
    with open('phone_book.txt', 'w', encoding='utf-8') as data:
        for i in phone_book:
            data.write(i)


def show_phone_book():
    print(phone_book)
    if len(phone_book) == 0:
        print('Вы не открыли файл, либо файл пустой!')
    else:
        for i in phone_book:
            print(' '.join(i.split(';')))


def add_phone_book():
    if len(phone_book) == 0:
        print('Вы не открыли файл, либо файл пустой!')
    else:
        user_info = input('Введите данные нового контакта: ')
        user_info = ';'.join(user_info.split(' '))
        phone_book.append(user_info + '\n')


def change_phone_book():
    user_info = input('Введите номер контакта, который хотите изменить: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])
            print(i)
            new_user_info = input('Введите новый номер контакта: ')
            phone_book[i] = phone_book[i].replace(user_info, new_user_info)


def search_phone_book():
    user_info = input('Введите номер, по которым вы хотите найти контакт: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])


def delete_phone_book():
    user_info = input('Введите номер контакта, который вы хотите уалить: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])
            question = input('Действительно удалить контакт? y - да, n - нет: ')
            if question == 'y':
                phone_book.pop(i)
                break
            else:
                break


phone_book = open_phone_book()


def print_menu():
    print('Это телефонный справочник. Выберите действие, которое нужно совершить:\n'
          '1. Открыть файл\n'
          '2. Сохранить файл\n'
          '3. Показать контакты\n'
          '4. Добавить контакты\n'
          '5. Изменить контакты\n'
          '6. Найти контакт\n'
          '7. Удалить контакт\n'
          '8. Выход')
    data = int(input('Введите номер необходимого действия: '))
    return data


while True:
    user_choice = print_menu()
    match user_choice:
        case 1:
            print('Открыть файл')
            open_phone_book()
        case 2:
            print('Сохранить файл')
            save_phone_book()
        case 3:
            print('Показать контакты')
            show_phone_book()
        case 4:
            print('Добавить контакты')
            add_phone_book()
        case 5:
            print('Изменить контакты')
            change_phone_book()
        case 6:
            print('Найти контакт')
            search_phone_book()
        case 7:
            print('Удалть контакт')
            delete_phone_book()
        case 8:
            print('Выход')
            break
