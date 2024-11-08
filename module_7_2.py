def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'wb') as f:
        for line_number, line in enumerate(strings, start=1):
            # Сохраняем текущую позицию в байтах
            byte_position = f.tell()

            # Записываем строку в файл (кодировка UTF-8)
            f.write((line + '\n').encode('utf-8'))

            # Сохраняем информацию о позиции и строке
            strings_positions[(line_number, byte_position)] = line

    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)