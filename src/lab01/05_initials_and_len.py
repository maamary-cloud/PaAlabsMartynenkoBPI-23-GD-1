parts = input("ФИО: ").split()
fio = " ".join(parts)
initials = ""
for part in parts:
    initials += part[0].upper()
print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len(fio)}")
