from collections import deque

def decrypt_message(encrypted_file, decryption_deck):
    decrypted_message = ""

    # Создаем дек для удобства расшифровки
    deck = deque(decryption_deck)

    # Открываем файл с зашифрованным сообщением
    with open(encrypted_file, 'r') as file:
        encrypted_message = file.read().strip()


    for char in encrypted_message:
        # Ищем позицию символа в деке
        index = deck.index(char)
        # Получаем следующий символ через один по часовой стрелке
        decrypted_char = deck[(index - 1) % len(deck)]
        # Добавляем расшифрованный символ к итоговому сообщению
        decrypted_message += decrypted_char

    return decrypted_message


decryption_deck = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encrypted_file = 'encrypted_message.txt'
decrypted_message = decrypt_message(encrypted_file, decryption_deck)
print("Расшифрованное сообщение:", decrypted_message)
