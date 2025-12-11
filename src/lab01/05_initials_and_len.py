name = input("ФИО: ").strip()
part = name.split()
length = len("".join(part)) + 2
ini = "".join([i[0].upper() for i in part])
print(f"Инициалы: {ini}")
print(f"Длина (символов): {length}")
