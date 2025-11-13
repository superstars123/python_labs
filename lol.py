json_path = 'C:/Users/1/python_labs/data/samples/people.json'

# Читаем сырое содержимое файла
with open(json_path, 'r', encoding='utf-8') as f:
    raw_content = f.read()
    print(f"Сырое содержимое файла: '{raw_content}'")
    print(f"Длина содержимого: {len(raw_content)} символов")
    print(f"Реально пустой?: {len(raw_content) == 0}")