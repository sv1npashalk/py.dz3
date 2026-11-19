text = input("Введіть рядок: ")

if text:
    first_char = text[0]
    count = text.count(first_char)
    print(f"Перший символ '{first_char}' зустрічається у рядку {count} раз(ів).")
else:
    print("Ви ввели порожній рядок.")
