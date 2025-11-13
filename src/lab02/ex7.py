def format_record(student: tuple[str, str, float]) -> str:
    if len(student) != 3:
        raise "ValueError"
    if not (isinstance(student[0], str) and isinstance(student[1], str) and isinstance(student[2],float)):
        return "TypeError"
    fio_parts = student[0].split()
    result = fio_parts[0].title() + " " + fio_parts[1][0].upper()
    if len(fio_parts) == 3:
        result += "." + fio_parts[2][0].upper() + "., "
    else:
        result += "., "
    result += "гр. " + student[1] + ", GPA " + f"{round(student[2], 2):.2f}"
    return result

a = ("Иванов Иван Иванович", "BIVT-25", 4.6)
b = ("Петров Пётр", "IKBO-12", 5.0)
c = ("Петров Пётр Петрович", "IKBO-12", 5.0)
d = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
x = (" ", " ",1)
print(format_record(a))
print(format_record(b))
print(format_record(c))
print(format_record(d))
print(format_record(x))