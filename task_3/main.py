# Скорик
import json
import os

print("start code ...")

filename = "stars.json"

if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        stars = json.load(f)
else:
    stars = []

operation_count = 0

while True:
    print("\nМеню:")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю id")
    print("3. Добавить запись")
    print("4. Удалить запись по полю id")
    print("5. Выйти из программы")
    
    choice = input("Выберите пункт меню (1-5): ").strip()
    
    if choice == "1":
        print("\n============== Все записи ==============")
        if not stars:
            print("Нет записей.")
        else:
            for star in stars:
                visible_str = "видна без телескопа" if star["is_visible"] else "не видна без телескопа"
                print(f"ID: {star['id']}")
                print(f"Название: {star['name']}")
                print(f"Созвездие: {star['constellation']}")
                print(f"Видимость: {visible_str}")
                print(f"Радиус (в солнечных): {star['radius']}")
                print("-" * 40)
        operation_count += 1

    elif choice == "2":
        try:
            target_id = int(input("Введите ID звезды: "))
            found = False
            for index, star in enumerate(stars):
                if star["id"] == target_id:
                    print(f"\n============== Найдено ==============")
                    print(f"Позиция в списке: {index + 1}")
                    visible_str = "видна без телескопа" if star["is_visible"] else "не видна без телескопа"
                    print(f"ID: {star['id']}")
                    print(f"Название: {star['name']}")
                    print(f"Созвездие: {star['constellation']}")
                    print(f"Видимость: {visible_str}")
                    print(f"Радиус (в солнечных): {star['radius']}")
                    found = True
                    break
            if not found:
                print("\n============== Не найдено ===============")
        except ValueError:
            print("Некорректный ввод ID.")
        operation_count += 1

    elif choice == "3":
        try:
            new_id = max([s["id"] for s in stars], default=0) + 1
            name = input("Введите название звезды: ").strip()
            constellation = input("Введите созвездие: ").strip()
            is_visible_input = input("Видна без телескопа? (да/нет): ").strip().lower()
            is_visible = True if is_visible_input in ("да", "yes", "y", "1") else False
            radius = float(input("Введите радиус в солнечных радиусах: "))
            new_star = {
                "id": new_id,
                "name": name,
                "constellation": constellation,
                "is_visible": is_visible,
                "radius": radius
            }
            stars.append(new_star)
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(stars, f, ensure_ascii=False, indent=4)
            print("Запись успешно добавлена.")
        except ValueError:
            print("Ошибка: радиус должен быть числом.")
        operation_count += 1

    elif choice == "4":
        try:
            target_id = int(input("Введите ID звезды для удаления: "))
            initial_len = len(stars)
            stars = [s for s in stars if s["id"] != target_id]
            if len(stars) == initial_len:
                print("\n============== Не найдено ===============")
            else:
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(stars, f, ensure_ascii=False, indent=4)
                print("Запись успешно удалена.")
        except ValueError:
            print("Некорректный ввод ID.")
        operation_count += 1

    elif choice == "5":
        print(f"\nВыполнено операций: {operation_count}")
        print("... end code")
        break

    else:
        print("Некорректный выбор. Пожалуйста, введите число от 1 до 5.")